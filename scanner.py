import yfinance as yf
VOLUME_MULTIPLIER = 1.2
stocks = [ "TCS.NS","INFY.NS","RELIANCE.NS","SBIN.NS","HDFCBANK.NS","AEGISLOG.NS"]
for stock in stocks:
    signals = []
    data = yf.download(stock, period="6mo", progress=False)
    data.columns = data.columns.get_level_values(0)
    data = data.dropna(subset=["Close"])
    data["ma20"] = data["Close"].rolling(20).mean()
    data["ma50"] = data["Close"].rolling(50).mean()
    data["vol20"] = data["Volume"].rolling(20).mean()
    data["delta"] = data["Close"].diff()
    data["gain"] = data["delta"].clip(lower=0)
    data["loss"] = -data["delta"].clip(upper=0)
    data["avg_gain"] = data["gain"].rolling(14).mean()
    data["avg_loss"] = data["loss"].rolling(14).mean()
    data["rs"] = data["avg_gain"] / data["avg_loss"]
    data["rsi"] = 100 - (100 / (1 + data["rs"]))
    latest = data.iloc[-1]
    avg_volume = latest["vol20"]
    today_volume = latest["Volume"]
    previous_high = data["High"][:-1].max()
    score = 0
    if (latest["Close"] > latest["ma20"]):
        score += 1
        signals.append("✅ Above 20 MA")
    else:
        signals.append("❌ Below 20 MA")
    if (latest["Close"] > latest["ma50"]):
        score += 1
        signals.append("✅ Above 50 MA")
    else:
        signals.append("❌ Below 50 MA")
    if (latest["Close"] > previous_high):
        score += 1
        signals.append("✅ Previous High Breakout")
    else:
        signals.append("❌ No Previous High Breakout")
    if (today_volume > VOLUME_MULTIPLIER * avg_volume):
        score += 1
        signals.append("✅ Volume Breakout")
    else:
        signals.append("❌ No Volume Breakout")
    if 50 <= latest["rsi"] <= 70:
        score += 1
        signals.append("✅ Healthy RSI")
    else:
        signals.append("❌ RSI not in swing range")
    print("=" * 50)
    print(f"{stock:^50}")
    print("=" * 50)
    print(f"{'Score':20}: {score}/5")
    print(f"{'Close':20}: {latest['Close']:.2f}")
    print(f"{'ma20':20}: {latest['ma20']:.2f}")
    print(f"{'ma50':20}: {latest['ma50']:.2f}")
    print(f"{'RSI':20}: {latest['rsi']:.2f}")
    print(f"{'Previous High':20}: {previous_high:.2f}")
    print(f"{'Todays Volume':20}: {today_volume:,.0f}")
    print(f"{'20D Avg Volume':20}: {avg_volume:,.0f}")
    print("-" * 45)
    print("\nSignals:")

    for signal in signals:
        print(signal)