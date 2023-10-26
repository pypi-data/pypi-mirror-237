from abc import ABCMeta, abstractmethod


class CommissionModel(object, metaclass=ABCMeta):
    """ABC for commission models

    Commission models are responsible for accepting order/transaction pairs and
    calculating how much commission should be charged to an algorithm's account
    on each transaction.
    """

    @abstractmethod
    def calculate(self, ) -> float:
        """
        Returns
        -------
        amount_charged: float
            The additional commission, in yuans, that we should attribute to this order.
        """
        raise NotImplementedError(f"{self.__name__}.calculate")
    

class PercentageCommissionModel(CommissionModel):

    def __init__(self, buy_commission=0.001, sell_commission=0.001):
        self.buy_commission = buy_commission
        self.sell_commission = sell_commission

    def calculate(self, nums, fill_prices):
        buy_orders_mask = nums > 0
        sell_orders_mask = nums < 0
        buy_cost = nums * buy_orders_mask * fill_prices * (1 + self.buy_commission)
        sell_cost = nums * sell_orders_mask * fill_prices * (1 - self.sell_commission)
        return buy_cost + sell_cost


