def calculate_rsi(data):

    data["delta"] = data["Close"].diff()
    data["gain"] = data["delta"].clip(lower=0)
    data["loss"] = -data["delta"].clip(upper=0)
    data["avg_gain"] = data["gain"].rolling(14).mean()
    data["avg_loss"] = data["loss"].rolling(14).mean()
    data["rs"] = data["avg_gain"] / data["avg_loss"]
    data["rsi"] = 100 - (100 / (1 + data["rs"]))
    return data

def calculate_atr(data):
    data["previous_close"] = data["Close"].shift(1)
    data["high_low"] = data["High"] - data["Low"]
    data["high_previous_close"] = (data["High"] - data["previous_close"]).abs()
    data["low_previous_close"] = (data["Low"] - data["previous_close"]).abs()
    data["tr"] = data[["high_low","high_previous_close","low_previous_close"]].max(axis=1)
    data["atr"] = data["tr"].rolling(14).mean()
    data["stoploss"] = data["Close"] - 2 * data["atr"]
    data["target"] = data["Close"] + 4 * data["atr"]
    data["risk"] = data["Close"] - data["stoploss"]
    data["reward"] = data["target"] - data["Close"]
    data["rr"] = data["reward"] / data["risk"]
    return data

def calculate_macd(data):

    ema12 = data["Close"].ewm(span=12, adjust=False).mean()
    ema26 = data["Close"].ewm(span=26, adjust=False).mean()
    data["macd"] = ema12 - ema26
    data["signal"] = data["macd"].ewm(span=9, adjust=False).mean()
    data["histogram"] = data["macd"] - data["signal"]
    return data

def calculate_relative_strength(data, nifty_data):

    if len(data) < 21 or len(nifty_data) < 21:
        return None

    today_close = data["Close"].iloc[-1]
    close_20_days_ago = data["Close"].iloc[-21]
    nifty_today_close = nifty_data["Close"].iloc[-1]
    nifty_close_20_days_ago = nifty_data["Close"].iloc[-21]
    stock_return = ((today_close - close_20_days_ago) / close_20_days_ago) * 100
    nifty_return = ((nifty_today_close - nifty_close_20_days_ago) / nifty_close_20_days_ago) * 100
    rs = stock_return - nifty_return
    return rs

def calculate_52_week_high(data):
    previous_52_week_high = data["High"][-253:-1].max()
    return previous_52_week_high

def calculate_relative_volume(data):
    todays_volume = data["Volume"].iloc[-1]
    avg_20_day_volume = data["Volume"].rolling(20).mean().iloc[-1]
    rvol = todays_volume / avg_20_day_volume
    return rvol