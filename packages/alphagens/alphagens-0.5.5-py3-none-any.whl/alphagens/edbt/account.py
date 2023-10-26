import pandas as pd
from .engine import SimulationEngine
from .model.commission import PercentageCommissionModel

    
class Account:
    """统计账户信息
    """
    def __init__(self, 
            engine: SimulationEngine,
            capital_base: float = 1e6,
            commission: tuple = (.0, .0),
            slippage: float = 0.0,
        ):
        self._engine = engine
        self._data_portal = self._engine._data_portal
        self.positions = pd.Series(0, index=self._data_portal.universe, dtype=int)
        self.commission_model = PercentageCommissionModel(commission[0], commission[1])
        self.slippage = slippage
        self.cash = capital_base

        self._dirty = True
        self._order_lists = []
        self._filled_order_lists = []

    @property
    def current_date(self):
        return self._engine.current_date

    @property
    def spot_prices(self):
        return self._engine.spot_prices

    def _update(self):
        self._dirty = True
        try:
            filled_orders = self._filled_order_lists.pop()
            assets = filled_orders.index
            nums = filled_orders["nums"]
            fill_price = filled_orders["fill_price"]
            total_cost = self.commission_model.calculate(nums, fill_price).sum() # 还可以加入成本, 印花税
            self.cash -= total_cost
            self.positions[assets] += nums
        except IndexError:
            pass
    
    def on_session_start(self):
        pass
        # self._previous_total_returns = self.returns

    def on_session_end(self):
       self._update()

    def order(self, amounts: pd.Series):
        self._order_lists.append(amounts)

    def order_target_pct_to(self, target_weights: pd.Series):
        assert target_weights.sum() <= 1.001
        assets = target_weights.index
        portfolio_value = self.portfolio_value
        spot_prices = self._engine.spot_prices.loc[assets]
        nums = (target_weights * portfolio_value / spot_prices).fillna(0).astype(int) - self.positions.loc[assets]
        self.order(nums)

    @property
    def portfolio_value(self):
        return self.cash + (self.positions * self.spot_prices).sum()
    
    @property
    def current_portfolio_weight(self):
        position_values = self.positions * self.spot_prices
        return position_values / position_values.sum()

