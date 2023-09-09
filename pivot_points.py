import pandas as pd
import yfinance as yf

#didziausia problema su pivot points indikatorium, jog sis yra apskaiciuojamas pagal formule ir praeitos savaites indicatoriaus duomenys turi buti pateikti 
# naujai.
#  
weekly_data = yf.download("BTC-USD", start="2023-01-02", end="2023-02-13", interval = "1wk")
weekly_data.drop(["Adj Close", "Volume"], inplace=True, axis=1)
weekly_data

print(weekly_data)

#...

hourly_data = yf.download("BTC-USD", start="2023-01-25", end="2023-02-07", interval = "1h")
hourly_data.drop(["Adj Close", "Volume"], inplace=True, axis=1)
hourly_data

print(hourly_data)

#... suskaiciuojam weekly pivots on  weekly timeframe. 



weekly_data["PP"] = (weekly_data["High"] + weekly_data["Low"] + weekly_data["Close"]) / 3

weekly_data["R1"] = weekly_data["PP"] * 2 - weekly_data["Low"]
weekly_data["S1"] = weekly_data["PP"] * 2 - weekly_data["High"]

weekly_data["R2"] = weekly_data["PP"] + (weekly_data["High"] - weekly_data["Low"])
weekly_data["S2"] = weekly_data["PP"] - (weekly_data["High"] - weekly_data["Low"])

weekly_data

print(weekly_data)

#... perstumem pivot point  praeitos savaites duomenys i prieki

weekly_data["PP"] = weekly_data["PP"].shift(1)
weekly_data["R1"] = weekly_data["R1"].shift(1)
weekly_data["R2"] = weekly_data["R2"].shift(1)
weekly_data["S1"] = weekly_data["S1"].shift(1)
weekly_data["S2"] = weekly_data["S2"].shift(1)

weekly_data

print(weekly_data)

#...

weekly_data.dropna(inplace=True)
weekly_data = weekly_data[["PP", "S1", "S2", "R1", "R2"]]
weekly_data
print(weekly_data)

#... sujungiu 1hr timeframe duomenis su savaitiniais pivot points. 

plot_data = pd.merge_asof(hourly_data, weekly_data, left_index=True, right_index=True)
plot_data
print(plot_data)


# import plotly.graph_objects as go

# fig = go.Figure(data=[go.Candlestick(x=plot_data.index,
#                 open=plot_data["Open"],
#                 high=plot_data["High"],
#                 low=plot_data["Low"],
#                 close=plot_data["Close"],
#                 name="OHLC")])

# fig.update_layout(xaxis_rangeslider_visible=False)

# fig.add_trace(go.Scatter(
#     x=plot_data.index,
#     y=plot_data.PP,
#     marker=dict(color="orange",size=4),
#     mode="markers",
#     name="PP"
# ))

# fig.add_trace(go.Scatter(
#     x=plot_data.index,
#     y=plot_data.S1,
#     marker=dict(color="red",size=4),
#     mode="markers",
#     name="S1"
# ))

# fig.add_trace(go.Scatter(
#     x=plot_data.index,
#     y=plot_data.S2,
#     marker=dict(color="red",size=4),
#     mode="markers",
#     name="S2"
# ))

# fig.add_trace(go.Scatter(
#     x=plot_data.index,
#     y=plot_data.R1,
#     marker=dict(color="green",size=4),
#     mode="markers",
#     name="R1"
# ))

# fig.add_trace(go.Scatter(
#     x=plot_data.index,
#     y=plot_data.R2,
#     marker=dict(color="green",size=4),
#     mode="markers",
#     name="R2"
# ))

# fig.show()

