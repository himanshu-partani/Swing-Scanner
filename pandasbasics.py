import pandas as pd

data = pd.read_csv("data/stocks.csv")

print(data)
print(data["Ticker"])
print(type(data))
print(type(data["Ticker"]))

for stock in data["Ticker"]:
    print(stock)
    
import yfinance as yf

data = yf.download(
    "KALYANKJIL.NS",
    period="1mo",
    interval="1d",
    progress=False,
    auto_adjust=False
)

print(data.index[-1])
print(data.tail())