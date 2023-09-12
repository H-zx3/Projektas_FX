from backtesting import Backtest, Strategy
# from backtesting.test import GOOG
from pivot_points import plot_data
from backtesting.lib import crossover # sutaupo laiko isimportuojam prebuilt crossover strategies
import talib

print(plot_data)
ema12 = 10
ema36 = 20


class  EmaCross(Strategy):
    
    def init(self):      
        self.ema1 = self.I(talib.EMA, self.data.Close,ema12 )
        self.ema2 = self.I(talib.EMA,  self.data.Close,ema36,)
        self.pp = self.data.PP
#...
    def next(self):        
# sekancios eilutes logika turi buti tokia: is plot_data paimam 1 hr rinkos pokyciu uzdarymo kaina ir ji turi buti didesne nei PRAEITOS ir -       
#-UZPRAEITOS savaites pivot point indicatoriaus PP 'parodymai. Mano manymu self.pp[-2] ir self.pp[-3] turetu tai ir atitikti.        
        if self.data.Close[-1] > self.pp[-2] and self.data.Close[-1] > self.pp[-3]:  
            if crossover(self.ema1, self.ema2):
            # self.position.close()
                self.buy()
        
            elif crossover(self.ema2, self.ema1):
                self.position.close()
            # self.sell()   
        
    
   

bt = Backtest(plot_data, EmaCross, cash=100000)    

stats = bt.run()
print(stats)
bt.plot()  #jai neplotina isirasyti pip3 install bokeh==3.1.1     

