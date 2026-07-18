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

    # V4 compatible
    data["macd_histogram"] = data["macd"] - data["signal"]
    # Backward compatibility
    data["histogram"] = data["macd_histogram"]
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

def calculate_consolidation(data):
    highest_high = data["High"][-16:-1].max()
    lowest_low = data["Low"][-16:-1].min()
    range_percent = ((highest_high - lowest_low) / lowest_low) * 100
    average_atr = data["atr"][-16:-1].mean()
    latest_close = data["Close"].iloc[-1]
    atr_percent = (average_atr / latest_close) * 100
    return round(range_percent, 2), round(atr_percent, 2)

import numpy as np
import pandas as pd
def calculate_adx(data, period=14):
    """
    Calculate Average Directional Index (ADX) using Wilder's method.

    Parameters:
        data (pd.DataFrame): OHLCV dataframe
        period (int): ADX lookback period (default = 14)

    Returns:
        pd.DataFrame:
            Original dataframe with:
            - plus_di
            - minus_di
            - adx
    """

    high = data["High"]
    low = data["Low"]
    close = data["Close"]

    # -----------------------------
    # True Range (TR)
    # -----------------------------
    tr1 = high - low
    tr2 = (high - close.shift()).abs()
    tr3 = (low - close.shift()).abs()

    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

    # -----------------------------
    # Directional Movement (+DM/-DM)
    # -----------------------------
    up_move = high.diff()
    down_move = -low.diff()

    plus_dm = np.where(
        (up_move > down_move) & (up_move > 0),
        up_move,
        0.0
    )

    minus_dm = np.where(
        (down_move > up_move) & (down_move > 0),
        down_move,
        0.0
    )

    plus_dm = pd.Series(plus_dm, index=data.index)
    minus_dm = pd.Series(minus_dm, index=data.index)

    # -----------------------------
    # Wilder's Smoothing
    # -----------------------------
    atr = tr.ewm(alpha=1 / period, adjust=False).mean()

    plus_dm_smoothed = plus_dm.ewm(alpha=1 / period, adjust=False).mean()
    minus_dm_smoothed = minus_dm.ewm(alpha=1 / period, adjust=False).mean()

    # -----------------------------
    # Directional Indicators
    # -----------------------------
    plus_di = 100 * (plus_dm_smoothed / atr)
    minus_di = 100 * (minus_dm_smoothed / atr)

    # -----------------------------
    # DX
    # -----------------------------
    dx = (
        (plus_di - minus_di).abs()
        / (plus_di + minus_di)
    ) * 100

    # -----------------------------
    # ADX
    # -----------------------------
    adx = dx.ewm(alpha=1 / period, adjust=False).mean()

    data["plus_di"] = plus_di
    data["minus_di"] = minus_di
    data["adx"] = adx

    return data


def calculate_obv(data):
    """
    Calculate On-Balance Volume (OBV).

    Parameters:
        data (pd.DataFrame): OHLCV dataframe

    Returns:
        pd.DataFrame:
            Original dataframe with:
            - obv
    """

    # Initialize OBV
    obv = [0]

    # Calculate cumulative OBV
    for i in range(1, len(data)):
        if data["Close"].iloc[i] > data["Close"].iloc[i - 1]:
            obv.append(obv[-1] + data["Volume"].iloc[i])

        elif data["Close"].iloc[i] < data["Close"].iloc[i - 1]:
            obv.append(obv[-1] - data["Volume"].iloc[i])

        else:
            obv.append(obv[-1])

    data["obv"] = obv        
    data["obv_ema20"] = data["obv"].ewm(span=20, adjust=False).mean()
    return data
