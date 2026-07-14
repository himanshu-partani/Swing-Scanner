import pandas as pd
import yfinance as yf

from indicators import (
    calculate_rsi,
    calculate_atr,
    calculate_macd,
    calculate_relative_strength,
    calculate_52_week_high,
    calculate_relative_volume,
    calculate_consolidation,
    
)
from market_structure import(
    find_swing_points,
    group_swing_points,
    find_nearest_zones,
    filter_zones,
    calculate_zone_distance,
)

LOOKBACK_3_MONTHS = 63
VOLUME_MULTIPLIER = 1.2
CONSOLIDATION_RANGE_THRESHOLD = 5
CONSOLIDATION_ATR_THRESHOLD = 2
MIN_SUPPORT_TOUCHES = 2
MIN_RESISTANCE_TOUCHES = 2

# Download Nifty data once
nifty_data = yf.download("^NSEI", period="13mo", progress=False)
nifty_data.columns = nifty_data.columns.get_level_values(0)
nifty_data = nifty_data.dropna(subset=["Close"])

# Read watchlist
watchlist = pd.read_csv("data/stocks.csv")
stocks = watchlist["Ticker"]

for stock in stocks:
    signals = []
    try:
        data = yf.download(stock, period="13mo", progress=False)
        if data.empty:
            print(f"⚠️ {stock} returned no data. Skipping...")
            continue
        data.columns = data.columns.get_level_values(0)
        data = data.dropna(subset=["Close"])
        current_price = float(data["Close"].iloc[-1])

        # Moving Averages
        data["ma20"] = data["Close"].rolling(20).mean()
        data["ma50"] = data["Close"].rolling(50).mean()
        data["vol20"] = data["Volume"].rolling(20).mean()

        # Indicators
        data = calculate_rsi(data)
        data = calculate_atr(data)
        data = calculate_macd(data)
        rs = calculate_relative_strength(data, nifty_data)
        previous_52_week_high = calculate_52_week_high(data)
        relative_volume = calculate_relative_volume(data)
        consolidation_percent , atr_percent = calculate_consolidation(data)

        #Market Structure
        swing_lows , swing_highs = find_swing_points(data ,window = 5)
        support_zones = group_swing_points(swing_lows)
        resistance_zones = group_swing_points(swing_highs)
        support_zones = filter_zones(support_zones,MIN_SUPPORT_TOUCHES)
        resistance_zones = filter_zones(resistance_zones,MIN_RESISTANCE_TOUCHES)
        nearest_support, nearest_resistance = find_nearest_zones(support_zones,resistance_zones,current_price)
        support_distance, resistance_distance = calculate_zone_distance(nearest_support,nearest_resistance,current_price)

        latest = data.iloc[-1]
        avg_volume = latest["vol20"]
        todays_volume = latest["Volume"]
        previous_3_month_high = data["High"][-LOOKBACK_3_MONTHS:-1].max()
        score = 0

        # MA20
        if latest["Close"] > latest["ma20"]:
            score += 1
            signals.append("✅ Above 20 MA")
        else:
            signals.append("❌ Below 20 MA")

        # MA50
        if latest["Close"] > latest["ma50"]:
            score += 1
            signals.append("✅ Above 50 MA")
        else:
            signals.append("❌ Below 50 MA")

        # 3-Month High Breakout
        if latest["High"] > previous_3_month_high:
            score += 1
            signals.append("✅ 3-Month High Breakout")
        else:
            signals.append("❌ No 3-Month High Breakout")

        # Relative Volume
        if relative_volume > VOLUME_MULTIPLIER:
            score += 1
            signals.append("✅ Volume Breakout")
        else:
            signals.append("❌ No Volume Breakout")

        # RSI
        if 50 <= latest["rsi"] <= 70:
            score += 1
            signals.append("✅ Healthy RSI")
        else:
            signals.append("❌ RSI not in swing range")

        # MACD
        if latest["macd"] > latest["signal"]:
            score += 1
            signals.append("✅ Bullish MACD")
        else:
            signals.append("❌ Bearish MACD")

        # Relative Strength
        if rs is not None and rs > 0:
            score += 1
            signals.append("✅ Outperforming Nifty")
        elif rs is not None:
            signals.append("❌ Underperforming Nifty")
        else:
            signals.append("⚠️ Relative Strength Unavailable")

        # 52-Week High Breakout
        if latest["High"] > previous_52_week_high:
            score += 1
            signals.append("✅ 52-Week High Breakout")
        else:
            signals.append("❌ No 52-Week High Breakout")

        # Consolidation
        if (
            consolidation_percent < CONSOLIDATION_RANGE_THRESHOLD
            and atr_percent < CONSOLIDATION_ATR_THRESHOLD):
                score += 1
                signals.append("✅ Tight Consolidation")
        else:
                signals.append("❌ No Consolidation")



        # Market Structure

        # Strong Nearby Support
        if (
            nearest_support is not None
            and support_distance is not None
            and support_distance <= 5
            and nearest_support["strength"] != "Weak"
        ):
            score += 1
            signals.append("✅ Strong Nearby Support")
        else:
            signals.append("❌ Weak/Far Support")
        # Plenty of Upside
        if nearest_resistance is None:
            score += 1
            signals.append("✅ Clear Overhead (No Resistance Found)")
        elif resistance_distance is not None and resistance_distance >= 5:
            score += 1
            signals.append("✅ Plenty of Upside")
        else:
            signals.append("❌ Resistance Too Close")
        
        # -------------------- OUTPUT --------------------

        print("=" * 50)
        print(f"{stock:^50}")
        print("=" * 50)

        print(f"{'Score':20}: {score}/11")
        print(f"{'Close':20}: {latest['Close']:.2f}")
        print(f"{'MA20':20}: {latest['ma20']:.2f}")
        print(f"{'MA50':20}: {latest['ma50']:.2f}")
        print(f"{'RSI':20}: {latest['rsi']:.2f}")
        print(f"{'ATR':20}: {latest['atr']:.2f}")
        print(f"{'MACD':20}: {latest['macd']:.2f}")
        print(f"{'MACD Signal':20}: {latest['signal']:.2f}")
        print(f"{'Histogram':20}: {latest['histogram']:.2f}")

        if rs is None:
            print(f"{'RS vs Nifty':20}: N/A")
        else:
            print(f"{'RS vs Nifty':20}: {rs:.2f}%")

        print("-" * 45)

        print(f"{'Stop Loss':20}: {latest['stoploss']:.2f}")
        print(f"{'Target':20}: {latest['target']:.2f}")
        print(f"{'Risk':20}: {latest['risk']:.2f}")
        print(f"{'Reward':20}: {latest['reward']:.2f}")
        print(f"{'Reward : Risk':20}: {latest['rr']:.2f}")

        print(f"{'Previous 3M High':20}: {previous_3_month_high:.2f}")
        print(f"{'Previous 52W High':20}: {previous_52_week_high:.2f}")

        print(f"{'Todays Volume':20}: {todays_volume:,.0f}")
        print(f"{'20D Avg Volume':20}: {avg_volume:,.0f}")
        print(f"{'Relative Volume':20}: {relative_volume:.2f}x")

        print(f"{'Consolidation %':20}: {consolidation_percent:.2f}")
        print(f"{'ATR %':20}: {atr_percent:.2f}")

        print("---------------------------------------------")
        print("Market Structure")

        # Nearest Support
        if nearest_support is not None:
            print(
                f"{'Nearest Support':25}: "
                f"{nearest_support['zone_low']:.2f} - "
                f"{nearest_support['zone_high']:.2f}"
            )
            print(
                f"{'Support Touches':25}: "
                f"{nearest_support['touches']}"
            )
            print(
                f"{'Support Strength':25}: "
                f"{nearest_support['strength']}"
            )
            print(
                f"{'Distance to Support':25}: "
                f"{support_distance:.2f}%"
            )
        else:
            print(f"{'Nearest Support':25}: None")
            print(f"{'Support Touches':25}: -")
            print(f"{'Support Strength':25}: -")
            print(f"{'Distance to Support':25}: -")
                
        # Nearest Resistance
        if nearest_resistance is not None:
            print(
                f"{'Nearest Resistance':25}: "
                f"{nearest_resistance['zone_low']:.2f} - "
                f"{nearest_resistance['zone_high']:.2f}"
            )
            print(
                f"{'Resistance Touches':25}: "
                f"{nearest_resistance['touches']}"
            )
            print(
                f"{'Resistance Strength':25}: "
                f"{nearest_resistance['strength']}"
            )

            print(
            f"{'Distance to Resistance':25}:"
            f"{resistance_distance:.2f}%"
            )
        else:
            print(f"{'Nearest Resistance':25}: None")
            print(f"{'Resistance Touches':25}: -")
            print(f"{'Resistance Strength':25}: -")
            print(f"{'Distance to Resistance':25}: -")

        print("-" * 45)
        print()
        print("Trading Signals:")

        for signal in signals:
            print(signal)

    except Exception as e:
        print(e)
        print(f"⚠️ Could not scan {stock}. Skipping...")
        continue