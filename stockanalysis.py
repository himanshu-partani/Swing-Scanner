import yfinance as yf
tcs = yf.download("TCS.NS", period="3mo")
tcs.columns = tcs.columns.get_level_values(0)
tcs["20_MA"] = tcs["Close"].rolling(20).mean()
tcs["50_MA"] = tcs["Close"].rolling(50).mean()
latest = tcs.iloc[-1]

print("Today's Close:", latest["Close"])
print("20 MA:", latest["20_MA"])
print("50 MA:", latest["50_MA"])

if latest["Close"] > latest["20_MA"]:
    print("✅ Price is above 20 MA")
else:
    print("❌ Price is below 20 MA")