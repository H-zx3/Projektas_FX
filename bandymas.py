
from backtesting import Backtest, Strategy
# from backtesting.test import GOOG
from pivot_points import plot_data


from backtesting.lib import crossover # sutaupo laiko isimportuojam prebuilt crossover strategies. 

import talib

print(plot_data)
ema12 = 12
ema36 = 36


class  EmaCross(Strategy):
    
    def init(self):      
        self.ema1 = self.I(talib.EMA, self.data.Close,ema12 )
        self.ema2 = self.I(talib.EMA,  self.data.Close,ema36,)
#...
    def next(self):        
        if crossover(self.ema1, self.ema2):
            # self.position.close()
            self.buy()
        
        elif crossover(self.ema2, self.ema1):
            self.position.close()
            # self.sell()   
        
    
   

bt = Backtest(plot_data, EmaCross, cash=10000)    

stats = bt.run()
print(stats)
bt.plot()  #jai neplotina isirasyti pip3 install bokeh==3.1.1     
