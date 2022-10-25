"""
- Set of actions taken depending on context
- Next action will be taken on basis of current context
- It is compline with open closed design principle
"""
import math
from abc import ABCMeta, abstractmethod


class StockBuyStrategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, amount: int, price: int):
        pass


class AggressiveStockBuyStrategy(StockBuyStrategy):
    def execute(self, amount: int, price: int):
        bid_amount = amount
        bid_price = price
        stock_quantity = math.floor(bid_amount / bid_price)
        print(f"Placing bid for {stock_quantity} units at price {bid_price}")


class PassiveStockBuyStrategy(StockBuyStrategy):
    def execute(self, amount: int, price: int):
        bid_amount = int(amount * 0.5)
        bid_price = int(price * 0.9)
        stock_quantity = int(math.floor(bid_amount / bid_price))
        print(f"Placing bid for {stock_quantity} units at price {bid_price}")


class StrategyExecutor(object):
    def __init__(self, strategy: StockBuyStrategy = None):
        self.strategy = strategy

    def execute(self, amount: int, price: int):
        if not self.strategy:
            print("No strategy found!")
        else:
            self.strategy.execute(amount, price)


if __name__ == '__main__':
    investment = 1000000
    stock_price = 50000

    strategy_executor = StrategyExecutor()
    strategy_executor.execute(amount=investment, price=stock_price)

    strategy_executor = StrategyExecutor(strategy=AggressiveStockBuyStrategy())
    strategy_executor.execute(amount=investment, price=stock_price)

    strategy_executor = StrategyExecutor(strategy=PassiveStockBuyStrategy())
    strategy_executor.execute(amount=investment, price=stock_price)
