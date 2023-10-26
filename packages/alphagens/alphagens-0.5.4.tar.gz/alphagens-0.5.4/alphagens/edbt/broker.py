import pandas as pd
from .engine import SimulationEngine
from .account import Account


class SimulatedBroker:
    def __init__(self, 
        engine: SimulationEngine, 
        enforce_constraints: bool=False,
    ):
        self._engine: SimulationEngine = engine
        self._trading_constrints = self._engine._data_portal._trading_constraints
        self._enforce_constraints = enforce_constraints

    def get_trading_constrints(self) -> pd.Series:
        return {key:val.loc[self._engine.current_date] for key, val in self._trading_constrints.items()}

    def handle_order(self, account: Account):
        try:
            target_nums = account._order_lists.pop()
            target_prices = self._engine.spot_prices.loc[target_nums.index] # 可以加入冲击模型得到fill_price
            
            # TODO: portable

            if self._enforce_constraints:
                sell_orders_mask = target_nums < 0
                buy_orders_mask = target_nums > 0

                constrains = self.get_trading_constrints()
                buy_constrains = constrains["limit_up"]
                # sell_constrains = constrains["limit_down"]
                buy_orders_mask *= buy_constrains

                # buy_orders_masked = buy_orders.intersection(constraints)
                target_nums[buy_orders_mask.astype(bool)] = 0
            fees = None
            filled_orders = pd.concat([target_nums, target_prices], axis=1)
            filled_orders.columns = ["nums", "fill_price"]
            account._filled_order_lists.append(filled_orders)
            
        except IndexError:
            pass
