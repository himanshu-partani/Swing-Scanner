import yfinance as yf

tcs = yf.download("TCS.NS", period="1mo")

print(tcs["Close"].min())