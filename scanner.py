import yfinance as yf
stocks = [
    "TCS.NS","INFY.NS","RELIANCE.NS","SBIN.NS","HDFCBANK.NS"
]
for stock in stocks:
    data = yf.download(stock, period="3mo")
    data.columns = data.columns.get_level_values(0)
    data["20_MA"] = data["Close"].rolling(20).mean()
    data["50_MA"] = data["Close"].rolling(50).mean()
    latest = data.iloc[-1]
    if latest["Close"] > latest["20_MA"] and latest["Close"] > latest["50_MA"]:
      print("--------------------------------")
      print(stock)
      print("Close :", round(latest["Close"], 2))
      print("20 MA :", round(latest["20_MA"], 2))
      print("50 MA :", round(latest["50_MA"], 2))
    