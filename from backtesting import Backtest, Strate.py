from backtesting import Backtest, Strategy
from backtesting.test import GOOG


from backtesting.lib import crossover # sutaupo laiko isimportuojam prebuilt crossover strategies. 

import talib

print(GOOG)
upper_bound = 70
lower_bound = 30


class RsiOscillator(Strategy):
    
    def init(self):      # init() is called once at the start suskaiciuojam indikatoriu reiksme
        self.rsi = self.I(talib.RSI, self.data.Close, 14)
#...
    def next(self):         # next() is called once per bar one by one 'apskaiciuoja' kriterijus ir nurodo ar pirkti-parduoti
        if crossover(self.rsi,upper_bound):
            self.position.close()

        elif crossover(lower_bound, self.rsi):
            self.buy()   
        
    


bt = Backtest(GOOG, RsiOscillator, cash=10_000)    

stats = bt.run()
print(stats)
bt.plot()  #jai neplotina isirasyti pip3 install bokeh==3.1.1     ..

