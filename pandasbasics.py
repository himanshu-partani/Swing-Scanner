import pandas as pd

data = pd.read_csv("data/stocks.csv")

print(data)
print(data["Ticker"])
print(type(data))
print(type(data["Ticker"]))

for stock in data["Ticker"]:
    print(stock)