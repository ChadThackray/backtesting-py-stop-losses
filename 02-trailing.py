
from backtesting import Backtest, Strategy
from backtesting.test import GOOG
from backtesting.lib import crossover, TrailingStrategy
import ta

print(GOOG)

class Strat(TrailingStrategy):
    
    def init(self):
        super().init()
        super().set_trailing_sl(5)

    def next(self):
        super().next()

        if self.position:
            pass
        else:
            price = self.data.Close[-1]
            self.buy(size = 1, sl = price - 10, tp = price + 20)
        
bt = Backtest(GOOG, Strat, cash=10_000)

bt.run()
bt.plot()
