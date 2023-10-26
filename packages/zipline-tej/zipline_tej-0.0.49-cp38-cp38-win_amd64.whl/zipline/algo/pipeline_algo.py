import numpy as np
import pandas as pd
import logbook

from zipline.utils.events import (
    date_rules,
    time_rules,
)

from zipline.algorithm import TradingAlgorithm
from zipline.sources.TEJ_Api_Data import get_Treasury_Return

from TejToolAPI.TejToolAPI import *

from zipline.data import bundles
from zipline.data.data_portal import DataPortal

from zipline.utils.calendar_utils import get_calendar
from zipline.utils.run_algo import  (get_transaction_detail,
                                     get_record_vars)

from zipline.pipeline.data import EquityPricing, TQDataSet, USEquityPricing
from zipline.pipeline.loaders import EquityPricingLoader
from zipline.pipeline.loaders.fundamentals import TQuantFundamentalsPipelineLoader
from zipline.finance import commission
from zipline.finance import slippage

from zipline.TQresearch.tej_pipeline import choose_loader as TQloader

from zipline.algorithm import TradingAlgorithm
from zipline.finance.trading import SimulationParameters

from zipline.utils.api_support import ZiplineAPI
from zipline.utils.input_validation import (
    expect_types,
    optional,
    expect_strictly_bounded
)

log = logbook.Logger("PipelineAlgo")

class TargetPercentPipeAlgo(TradingAlgorithm):    # TargetPercentPipelineAlgorithm
    """
    This algorithm uses the buy and sell lists provided by the pipeline, 
    places orders using the "order_target_percent" method, and rebalances periodically.
    """
    @expect_strictly_bounded(max_leverage=(0, None),)
    @expect_types(tradeday=optional(list),
                  stocklist=optional(list),
                  benchmark=optional(str),
                  volume_limit=optional(float),
                  price_impact=optional(float),
                  commission_cost=optional(float),
                  max_leverage=float,
                  adjust_amount=bool,
                  limit_buy_multiplier=optional(float),
                  limit_sell_multiplier=optional(float),
                  allow_short=bool,
                  custom_weight=bool,
                  cancel_datedelta=optional(int),
                  get_transaction_detail=bool,
                  )
    def __init__(self,
                 bundle_name='tquant',
                 start_session=None,
                 end_session=None,
                 trading_calendar=get_calendar('TEJ_XTAI'),
                 capital_base=1e7,
                 data_frequency='daily',
                 tradeday=None,
                 stocklist=None,
                 benchmark='IR0001',
                 volume_limit=0.025,
                 price_impact=0.1,
                 commission_cost=0.001425 + 0.003 / 2,
                 max_leverage=0.8,
                 adjust_amount=False,
                 limit_buy_multiplier=None,
                 limit_sell_multiplier=None,
                 allow_short=False,
                 cancel_datedelta=None,
                 custom_weight=False,
                 custom_loader=None,
                 pipeline=None,
                 analyze=None,
                 record_vars=None,
                 get_transaction_detail=False):

        self.bundle_name = bundle_name

        bundle = bundles.load(bundle_name)
        asset_finder = bundle.asset_finder
        sids = bundle.asset_finder.equities_sids
        assets = bundle.asset_finder.retrieve_all(sids)
        symbol_mapping_sid = {i.symbol:i.sid for i in assets}

        if start_session is None:
            start_session = self.default_pipeline_domain(trading_calendar).next_open(min([i.start_date for i in assets]))
        if end_session is None:
            end_session = self.default_pipeline_domain(trading_calendar).prev_open(max([i.end_date for i in assets]))

        data_portal = DataPortal(asset_finder=asset_finder,
                                 trading_calendar=trading_calendar,
                                 first_trading_day=bundle.equity_daily_bar_reader.first_trading_day,
                                 equity_daily_reader=bundle.equity_daily_bar_reader,
                                 adjustment_reader=bundle.adjustment_reader
                                 )

        sim_params = SimulationParameters(start_session=start_session,
                                          end_session=end_session,
                                          trading_calendar=trading_calendar,
                                          capital_base=capital_base,
                                          data_frequency=data_frequency,
                                          )
        
        self.custom_loader = custom_loader
        self.TQuantPipelineLoader = TQuantFundamentalsPipelineLoader(zipline_sids_to_real_sids=symbol_mapping_sid)

        super().__init__(data_portal = data_portal,
                         sim_params = sim_params,
                         get_pipeline_loader = self.choose_loader,
                         analyze = analyze
                        )

        self._record_vars = record_vars
        self.pipeline_loader = EquityPricingLoader.without_fx(bundle.equity_daily_bar_reader,
                                                              bundle.adjustment_reader,
                                                             )
        self.pipeline = pipeline

        if tradeday:
            self.tradeday = tradeday
        else:
            self.tradeday = sim_params.sessions # self.default_pipeline_domain(self.trading_calendar).all_sessions()

        self.benchmark = benchmark

        if stocklist:
            self.stocklist = stocklist
        else:
            self.stocklist = list(set([i.symbol for i in assets]) - set(self.benchmark))

        self.volume_limit = volume_limit
        self.price_impact = price_impact
        self.commission_cost = commission_cost
        self.max_leverage = max_leverage
        self.adjust_amount = adjust_amount
        self.limit_buy_multiplier = limit_buy_multiplier
        self.limit_sell_multiplier = limit_sell_multiplier
        self.allow_short = allow_short
        self.custom_weight = custom_weight
        self.cancel_datedelta = cancel_datedelta

        self.get_transaction_detail = get_transaction_detail

#         self.treasury_returns是原有的
        self.treasury_returns = get_Treasury_Return(start = sim_params.start_session,
                                                    end = sim_params.end_session,
                                                    rate_type = 'Time_Deposit_Rate',
                                                    term = '1y',
                                                    symbol = '5844'
                                                   )

    def __repr__(self):
        """
        N.B. this does not yet represent a string that can be used
        to instantiate an exact copy of an algorithm.

        However, it is getting close, and provides some value as something
        that can be inspected interactively.
        """
        return """
{class_name}(
    sim_params={sim_params},
    benchmark={benchmark},
    max_leverage={max_leverage},
    volume_limit={volume_limit},
    price_impact={price_impact},
    commission_cost={commission_cost},
    adjust_amount={adjust_amount},
    limit_buy_multiplier={limit_buy_multiplier},
    limit_sell_multiplier={limit_sell_multiplier},
    allow short or not（if "False" then long only）={allow_short},
    use custom weight or not（if not then "equal weighted"）={custom_weight},
    cancel_datedelta（if "None" then cancel at next rebalance date）={cancel_datedelta},
    stocklist={stocklist},
    tradeday={tradeday},
    get_transaction_detail={get_transaction_detail},
    blotter={blotter},
    recorded_vars={recorded_vars})
""".strip().format(class_name=self.__class__.__name__,
                           sim_params=self.sim_params,
                           benchmark=self.benchmark,
                           max_leverage=self.max_leverage,
                           volume_limit=self.volume_limit,
                           price_impact=self.price_impact,
                           commission_cost=self.commission_cost,
                           adjust_amount=self.adjust_amount,
                           limit_buy_multiplier=self.limit_buy_multiplier,
                           limit_sell_multiplier=self.limit_sell_multiplier,
                           allow_short=self.allow_short,
                           custom_weight=self.custom_weight,
                           cancel_datedelta=self.cancel_datedelta,
                           stocklist=self.stocklist,
                           tradeday=self.tradeday,
                           get_transaction_detail=self.get_transaction_detail,
                           blotter=repr(self.blotter),
                           recorded_vars=repr(self.recorded_vars),
                          )

    def choose_loader(self, column):
        """
        A function that is given a loadable term and returns a PipelineLoader to use to retrieve
        raw data for that term.

        Parameters
        ----------
        column：zipline.pipeline.data.Column
            An abstract column of data, not yet associated with a dataset.

        Reference
        ----------
        zipline.utils.run_algo.py
        """
        '''
        if column.name in EquityPricing._column_names:
            return self.pipeline_loader
        elif column.name in TQDataSet._column_names:
            print('Y')
            return self.TQuantPipelineLoader

        try:
            return self.custom_loader.get(column)
        except KeyError:
            raise ValueError("No PipelineLoader registered for column %s." % column)
        '''

        if column in USEquityPricing.columns:  # 不能用EquityPricing.columns
            return self.pipeline_loader
        elif (column in TQDataSet.columns):
            return self.TQuantPipelineLoader

        try:
            return self.custom_loader.get(column)
        except KeyError:
            raise ValueError("No PipelineLoader registered for column %s." % column)


    @staticmethod
    def calculate_next_trading_date(calendar, start_date, days_to_add):
        """
        For cancel_order and divest.
        """
        schedule = calendar.sessions_in_range(start_date, pd.Timestamp.max)

        start_date_timestamp = pd.Timestamp(start_date, tz="UTC")

#         檢查是否有足夠的交易日可供選擇
        if len(schedule) <= days_to_add:
            next_trading_date = pd.NaT
#             log.info("Not enough trading days available for the given days_to_add {} at {}".format(days_to_add,
#                                                                                                    start_date.strftime('%Y-%m-%d')))
        else:
            next_trading_date = schedule[schedule > start_date_timestamp][days_to_add - 1]

        return next_trading_date

    def initialize(self, *args, **kwargs):
        """
        Function that is called at the start of the simulation to
        setup the initial context.
        """
#         not necessary?
#         with ZiplineAPI(self):
#             self._initialize(self, *args, **kwargs)

        self.universe = [self.symbol(i) for i in self.stocklist]
        self.trades = {}

#         交易成本
        self.set_slippage(slippage.VolumeShareSlippage(volume_limit = self.volume_limit,
                                                       price_impact = self.price_impact))
        self.set_commission(commission.PerDollar(cost=self.commission_cost))

#         benchmark
        self.set_benchmark(self.symbol(self.benchmark))

#         schedule_function
#         not necessary!
#         self.schedule_function(func=self._handle_data,
#                                date_rule=date_rules.every_day(),
#                                time_rule=time_rules.market_open)

        self.schedule_function(func=self._record_vars,
                               date_rule=date_rules.every_day(),
                               time_rule=time_rules.market_close)

#         pipeline
        self.attach_pipeline(self.pipeline(), 'signals')

#         chk long
        if 'longs' not in self.pipeline().columns:
            raise ValueError('No PipelineLoader registered for column "longs", check func："pipeline"')

#         chk allow_short
        if (self.allow_short==True) & ('shorts' not in self.pipeline().columns):
            raise ValueError('No PipelineLoader registered for column "shorts", set "allow_short = False" instead or check func："pipeline"')

#         chk weights
        if ('long_weights' not in self.pipeline().columns) & (self.custom_weight==True):
            raise ValueError('No PipelineLoader registered for column "long_weights", set "custom_weight = False" instead or check func："pipeline"')
        elif (self.allow_short==True) & ('short_weights' not in self.pipeline().columns) & (self.custom_weight==True):
            raise ValueError('No PipelineLoader registered for column "short_weights", set "custom_weight = False" instead or check func："pipeline"')


#         避免handle_data裡面沒定義報錯。
        self.divest = []

    def get_target_amount(self, asset, count, max_leverage, weight_columns):
        """
        The func can determine how many shares of a stock need to be 
        purchased when using order_target_percent.
        """
        if not self.custom_weight:
            amount = self.calculate_order_target_percent_amount(asset,
                                                                1 / count * max_leverage)
        else:
            amount = self.calculate_order_target_percent_amount(asset,
                                                                self.output.loc[asset, weight_columns] * max_leverage)

        return amount

    def get_limit(self, data, asset, amount):
        """
        The function calculates the limit price for buying or selling based on 
        "limit_buy_multiplier" and "limit_sell_multiplier".
        """
        if amount > 0:
#             data.current用price避免close沒價格，但理應不會有這情況
            limit_price = data.current(asset, 'price') * self.limit_buy_multiplier
        elif amount < 0:
            limit_price = data.current(asset, 'price') * self.limit_sell_multiplier
        else:
            limit_price = None

        if np.isnan(limit_price):
            limit_price = None

        return limit_price

    def get_adj_amount(self, data, asset, amount):
        """
        The function adjusts the number of shares placed in an order based on the price 
        difference between the time of placing the order and the time of execution, 
        reducing overbought and oversold issues.
        """
#         預計成交時價格
        transaction_price = self.data_portal.get_spot_value(assets = asset,
                                                            field = 'close',
                                                            dt = self.calculate_next_trading_date(self.trading_calendar,
                                                                                                  self.get_datetime().strftime('%Y-%m-%d'),
                                                                                                  1),
                                                            data_frequency = self.data_frequency)

        if np.isnan(transaction_price)==False:
    #         前一筆價格
            order_price = data.current(asset, "price")

    #         價格變化
            chg = transaction_price / order_price

    #         調整下單數，並捨去（Round a to the nearest integer if that integer is within an epsilon of 1e-4）
            adj_amount = self.round_order(amount / chg)

        else:
            adj_amount = amount

        return adj_amount


    def exec_trades(self, data, asset, count, long_short):
        """
        Place orders for assets
        """
        if long_short=='long':
            max_leverage = self.max_leverage * 1
            weight_columns = 'long_weights'

        elif long_short=='short':
            max_leverage = self.max_leverage * -1  
            weight_columns = 'short_weights'

        if data.can_trade(asset) and \
              asset in self.universe and not \
                self.get_open_orders(asset):

#             calculate order amount
            amount = self.get_target_amount(asset, count, max_leverage, weight_columns)

#             adjust_amount
            if self.adjust_amount==True:
                amount = self.get_adj_amount(data, asset, amount)

#             deal with limit price
            if ((amount > 0) & (self.limit_buy_multiplier is not None)) | \
               ((amount < 0) & (self.limit_sell_multiplier is not None)):
                limit_price = self.get_limit(data, asset, amount)

                self.order(asset,
                           amount,
                           limit_price = limit_price)
            else:
                self.order(asset,
                           amount)

    def handle_data(self, data):
        """
        Function called on every bar. This is where most logic should be
        implemented.    
        """
        self.list_longs = []

#         避免divest部位因除權調整而超賣，所以每天都先取消再下一單新的
        open_orders = self.get_open_orders()
        self.divest = [i for i in self.divest if i in open_orders.keys()]
        for asset in self.divest:
            for i in open_orders[asset]:
                self.cancel_order(i)
                try:
                    self.order_target(asset, 0)

                except Exception as e:
                    log.warn('{} {}'.format(self.get_datetime().date(), e))

#         自訂取消訂單時間
        if self.cancel_datedelta:
#             open_orders = self.get_open_orders()
            for asset in open_orders:
                for i in open_orders[asset]:
                    next_trading_date = self.calculate_next_trading_date(self.trading_calendar,
                                                                         i.created.strftime('%Y-%m-%d'),
                                                                         self.cancel_datedelta)

                    if self.get_datetime().strftime('%Y-%m-%d')>=next_trading_date.strftime('%Y-%m-%d'):

                        self.cancel_order(i)

                        str_log = """
                              Cancel_order: current time: {},
                              due to : created>=current time + cancel_datedelta({} days),
                              created: {}, asset: {}, amount: {}, filled: {}' 
                              """.strip().format(self.get_datetime().strftime('%Y-%m-%d'),
                                                 self.cancel_datedelta,
                                                 i.created.strftime('%Y-%m-%d'),
                                                 i.sid,
                                                 i.amount,
                                                 i.filled
                                                )

                        log.info(str_log)

#         再平衡
        if self.get_datetime().strftime('%Y-%m-%d') in self.tradeday: 
#             print('Current date(trade)＝' + str(self.get_datetime().date())) 

#             取消未成交的單
            if not self.cancel_datedelta:

                open_orders = self.get_open_orders()
                for asset in open_orders:
                    for i in open_orders[asset]:

                        self.cancel_order(i)

                        log.info('Cancel_order: current time: {} , created: {} , asset: {}, amount: {} , filled: {}'\
                                 .format(self.get_datetime().strftime('%Y-%m-%d'),
                                         i.created.strftime('%Y-%m-%d'),
                                         i.sid,
                                         i.amount,
                                         i.filled
                                        )
                                )

#             建立買進清單
            self.list_longs = list(set(self.output.loc[self.output['longs']==True].index.to_list()))

#             建立放空清單
            if self.allow_short:
                self.list_shorts = list(set(self.output.loc[self.output['shorts']==True].index.to_list()))
            else:
                self.list_shorts = []

#             建立賣出清單
            self.divest = list(set(self.portfolio.positions.keys()) - set(self.list_longs) - set(self.list_shorts))

#             下單
            N = len(self.list_longs)
            N_S = len(self.list_shorts)


            if (N > 0) | (N_S > 0):

                try:
                    for i in self.divest:
                        self.order_target(i, 0)

                    for i in self.list_longs:
                        self.exec_trades(data, i, N, 'long')

                    for i in self.list_shorts:
                        self.exec_trades(data, i, N_S, 'short') 
                        
                except Exception as e:
                    log.warn('{} {}'.format(self.get_datetime().date(), e))

            else:
                log.info(str(self.get_datetime().date()), 'both long positions and short positions = 0')

        else:
            pass

#         記錄每日權重
        self.daily_weights = self.portfolio.current_portfolio_weights

    def before_trading_start(self, data):
        """
        This is called once before each trading day (after initialize on the first day)
        """
#         compute any pipelines attached with eager=True. attach_pipeline->eager=True
        self.compute_eager_pipelines()

#         maybe not necessary!
        self._in_before_trading_start = True

        output = self.pipeline_output('signals')
        self.output = output

#         maybe not necessary!      
        self._in_before_trading_start = False

    def record_vars(self, data):
        """
        These values will appear in the performance packets and the performance
        dataframe passed to ``analyze`` and returned from
        :func:`~zipline.run_algorithm`.
        """    
        if self._record_vars is None:
            return

        self._record_vars(self, data)

    def analyze(self, perf):
        """
        Function that is called at the end of the backtest. This is passed
        the context and the performance results for the backtest.
        """
        if self.get_transaction_detail:
            positions, transactions, orders = get_transaction_detail(perf)
            self.positions, self.transactions, self.orders = positions, transactions, orders

        if self._analyze is None:
            return

        with ZiplineAPI(self):
            self._analyze(self, perf)
