
from backtesting import Backtest, Strategy
from backtesting.test import GOOG

print(GOOG)

class Strat(Strategy):
    
    def init(self):
        pass

    def next(self):

        if self.position:
            pass
        else:
            price = self.data.Close[-1]
            self.buy(size = 1, sl = price - 10, tp = price + 20)
        
bt = Backtest(GOOG, Strat, cash=10_000)

bt.run()
bt.plot()
