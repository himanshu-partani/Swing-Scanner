import yfinance as yf
stocks = [ "TCS.NS","INFY.NS","RELIANCE.NS","SBIN.NS","HDFCBANK.NS","AEGISLOG.NS"]
for stock in stocks:
    data = yf.download(stock, period="6mo")
    data.columns = data.columns.get_level_values(0)
    data = data.dropna(subset=["Close"])
    data["20_MA"] = data["Close"].rolling(20).mean()
    data["50_MA"] = data["Close"].rolling(50).mean()
    data["20_Volume"] = data["Volume"].rolling(20).mean()
    latest = data.iloc[-1]
    previous_high = data["High"][:-1].max()
    if (
    latest["Close"] > latest["20_MA"]
    and latest["Close"] > latest["50_MA"]
    and latest["Close"] > previous_high):
        print("--------------------------------")
        print(stock)
        print("Close :", round(latest["Close"],2))
        print("20 MA :", round(latest["20_MA"],2))
        print("50 MA :", round(latest["50_MA"],2))
        print("Previous 3M High :", round(previous_high,2))
    print("Todays Volume:" , round(latest["Volume"]))
    print("20 day avg Volume:" , round(latest["20_Volume"]))
    if( latest["Volume"] > 1.2 * latest["20_Volume"]):
        print(stock ,"volume breakout")