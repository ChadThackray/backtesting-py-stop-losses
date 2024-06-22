
from backtesting import Backtest, Strategy
from backtesting.test import GOOG
from backtesting.lib import crossover
import numpy as np
import ta

print(GOOG)

class TrailingStrategy(Strategy):
    __dollar_amount = 20.

    def init(self):
        super().init()

    def set_trailing_sl(self, dollar_amount: float = 6):
        self.__dollar_amount = dollar_amount

    def next(self):
        super().next()
        # Can't use index=-1 because self.__atr is not an Indicator type
        index = len(self.data)-1
        for trade in self.trades:
            if trade.is_long:
                trade.sl = max(trade.sl or -np.inf,
                               self.data.Close[index] - self.__dollar_amount)
            else:
                trade.sl = min(trade.sl or np.inf,
                               self.data.Close[index] + self.__dollar_amount)


class Strat(TrailingStrategy):

    def init(self):
        super().init()
        super().set_trailing_sl(2)

    def next(self):
        super().next()

        if self.position:
            pass
        else:
            price = self.data.Close[-1]
            self.buy(size = 1, sl = price - 50, tp = price + 20)

bt = Backtest(GOOG, Strat, cash=10_000)

bt.run()
bt.plot()