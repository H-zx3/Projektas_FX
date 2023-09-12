from backtesting import Backtest, Strategy
# from backtesting.test import GOOG
# from pivot_points import plot_data
import pandas as pd
from backtesting.test import GOOG

from backtesting.lib import crossover # sutaupo laiko isimportuojam prebuilt crossover strategies. 
plot_data = GOOG
import talib




# def PPSR(plot_data):  
#     PP = pd.Series((plot_data['High'] + plot_data['Low'] + plot_data['Close']) / 3)  
#     # R1 = pd.Series(2 * PP - df['Low'])  
#     # S1 = pd.Series(2 * PP - df['High'])  
#     # R2 = pd.Series(PP + df['High'] - df['Low'])  
#     # S2 = pd.Series(PP - df['High'] + df['Low'])  
#     # R3 = pd.Series(df['High'] + 2 * (PP - df['Low']))  
#     # S3 = pd.Series(df['Low'] - 2 * (df['High'] - PP))  
#     psr = {'PP':PP, }  #'R1':R1, 'S1':S1, 'R2':R2, 'S2':S2, 'R3':R3, 'S3':S3.
#     PSR = pd.DataFrame(psr)  
#     plot_data = plot_data.join(PSR)  
#     return plot_data

ema12 = 12
ema36 = 36

# plot_data = PPSR(plot_data)


class  EmaCross(Strategy):
    
    def init(self):      # init() is called once at the start suskaiciuojam indikatoriu reiksme
        self.ema1 = self.I(talib.EMA, self.data.Close,ema12 )
        self.ema2 = self.I(talib.EMA,  self.data.Close,ema36,)
        # self.pp = self.I(lambda: self.data.PP)  # Access the pivot points
#...
    def next(self):
        # Check if the close is above the pivot point
        
            # If ema1 crosses above ema2, buy
        if crossover(self.ema1, self.ema2):
            self.buy()
        # Else, if ema1 crosses below ema2, close the position
        elif crossover(self.ema2, self.ema1):
            self.position.close() 
        
    
   

bt = Backtest(plot_data, EmaCross, cash=100000)    

stats = bt.run()
print(stats)
bt.plot()  #jai neplotina isirasyti pip3 install bokeh==3.1.1     

