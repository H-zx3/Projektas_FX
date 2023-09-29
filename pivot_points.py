import yfinance as yf
import pandas as pd

def get_plot_data():
    
    weekly_data = yf.download("EURJPY=X", start="2023-01-02", end="2023-08-13", interval="1wk")
    weekly_data.drop(["Adj Close", "Volume"], inplace=True, axis=1)
    
    
    hourly_data = yf.download("EURJPY=X", start="2023-01-23", end="2023-08-13", interval="1h")
    hourly_data.drop(["Adj Close", "Volume"], inplace=True, axis=1)
    
    
    weekly_data["PP"] = (weekly_data["High"] + weekly_data["Low"] + weekly_data["Close"]) / 3
    weekly_data["R1"] = weekly_data["PP"] * 2 - weekly_data["Low"]
    weekly_data["S1"] = weekly_data["PP"] * 2 - weekly_data["High"]
    weekly_data["R2"] = weekly_data["PP"] + (weekly_data["High"] - weekly_data["Low"])
    weekly_data["S2"] = weekly_data["PP"] - (weekly_data["High"] - weekly_data["Low"])
    
    
    weekly_data["PP"] = weekly_data["PP"].shift(1)
    weekly_data["R1"] = weekly_data["R1"].shift(1)
    weekly_data["R2"] = weekly_data["R2"].shift(1)
    weekly_data["S1"] = weekly_data["S1"].shift(1)
    weekly_data["S2"] = weekly_data["S2"].shift(1)
    
    
    weekly_data.dropna(inplace=True)
    weekly_data = weekly_data[["PP", "S1", "S2", "R1", "R2"]]
    
    
    plot_data = pd.merge_asof(hourly_data, weekly_data, left_index=True, right_index=True)
    
   
    plot_data.dropna(inplace=True)
    plot_data.reset_index(inplace=True)
    
    return plot_data


plot_data = get_plot_data()
print(plot_data)



