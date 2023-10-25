import os
import joblib
import pandas as pd
import numpy as np
from .data_source.tushare import pro, Stock, Index
from .factor.preprocessing import get_clean_factor_and_forward_returns, get_clean_factor_and_current_returns
from .backtest import QuickBackTestor, QuickFactorTestor
from .utils.metrics import FactorMetrics, StrategyMetrics
from .utils.calendars import DEFAULT_CALENDAR
from .edbt import SimulationEngine, SimulatedBroker, Account, BaseStrategy


class Context:
    _instance = None

    def __new__(cls, start, end):
        cls.PATH = os.getcwd()
        cls.DATA_PATH = os.path.join(cls.PATH, "data")
        cls.START_DATE = start
        cls.END_DATE = end
        cls.BENCHMARK = "000300.SH"
        
        cls.TRADE_DATES = DEFAULT_CALENDAR.sessions_in_range(cls.START_DATE, cls.END_DATE)
        cls.REBALANCE_DATES = DEFAULT_CALENDAR.Weekly(cls.TRADE_DATES)
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

class DataPortal:
    def __init__(self, load_cov=False):
        print(f"loading data from {Context.DATA_PATH}")
        start_date = Context.START_DATE
        end_date = Context.END_DATE
        self._all_basic_data: pd.DataFrame = joblib.load(f"{Context.DATA_PATH}/tushare.ex_basic")
        self.prices: pd.DataFrame = self._all_basic_data["close"].unstack().fillna(method='ffill')
        self.index_weights = Index.components("000300.SH", "20180101")
        self.index_weights.index = [x[:-3] for x in self.index_weights.index]
        self.universe: list[str] = self.index_weights.index.to_list()
    
        self.factors: pd.DataFrame = joblib.load(f"{Context.DATA_PATH}/uqer.factor").loc[Context.TRADE_DATES]
        self.industry_map: pd.Series = joblib.load(f"{Context.DATA_PATH}/wind.industry_map")
        self.benchmark_returns: pd.Series = Index.history(["000300.SH"], start_date, end_date)[0]["close"].pct_change().fillna(0)
        if load_cov:
            self.covs = joblib.load(f"{Context.DATA_PATH}/tushare.cov_32")
            self.covs = self.covs.astype(np.float32)
        self._trading_constraints = {}

    def history(self, date, symbols: list, field: str, lookback: int = None):
        if lookback is not None:
            slice_dates = DEFAULT_CALENDAR.history(date, lookback)
            return self._all_basic_data.loc[(slice_dates, symbols), field]
    
    @property
    def factor_names(self):
        return self.factors.columns.to_list()
    
    def factor_get(self, factor_name, dates=None):
        # assert factor_name in self.factor_names
        if dates is not None:
            return self.factors.loc[(dates, slice(None)), factor_name]
        else:
            return self.factors[factor_name]
        
    def set_trading_constraints(self):
        self._trading_constraints["limit_up"] = (self._all_basic_data["pct_chg"] >= 10).unstack().fillna(True)
        self._trading_constraints["limit_down"] = (self._all_basic_data["pct_chg"] <= -10).unstack().fillna(True)
