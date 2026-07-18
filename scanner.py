from scoring import calculate_score
from report import build_report, print_report , print_market_summary ,print_top_setups
from ranking import sort_results
from config import (SCAN_MODE , OUTPUT_MODE )
from data_loader import (
    load_watchlist,
    download_nifty_data,
    download_market_data,
    load_nifty500
)

from indicators import (
    calculate_rsi,
    calculate_atr,
    calculate_macd,
    calculate_relative_strength,
    calculate_52_week_high,
    calculate_relative_volume,
    calculate_consolidation,
    calculate_adx,
    calculate_obv,
)
from market_structure import(
    find_swing_points,
    group_swing_points,
    find_nearest_zones,
    filter_zones,
    calculate_zone_distance,
)

from config import (
    LOOKBACK_3_MONTHS,
    VOLUME_MULTIPLIER,
    CONSOLIDATION_MAX_RANGE_PERCENT,
    CONSOLIDATION_MAX_ATR_PERCENT,
    MIN_SUPPORT_TOUCHES,
    MIN_RESISTANCE_TOUCHES,
    SWING_WINDOW,
)

# Download Nifty data once
nifty_data = download_nifty_data()

# Cheking 
if SCAN_MODE == "watchlist":
    stocks = load_watchlist()

elif SCAN_MODE == "nifty500":
    stocks = load_nifty500()
    print(f"Stocks Loaded: {len(stocks)}")

else:
    raise ValueError(f"Invalid SCAN_MODE: {SCAN_MODE}")

market_data = download_market_data(stocks)

results = []

for stock in stocks:
   
    try:
        data = market_data[stock]

        if data.empty:
            print(f"⚠️ {stock} returned no data. Skipping...")
            continue

        current_price = float(data["Close"].iloc[-1])

        # Moving Averages
        data["ma20"] = data["Close"].rolling(20).mean()
        data["ma50"] = data["Close"].rolling(50).mean()
        data["ma200"] = data["Close"].rolling(200).mean()
        data["vol20"] = data["Volume"].rolling(20).mean()

        # Indicators
        data = calculate_rsi(data)
        data = calculate_atr(data)
        data = calculate_macd(data)
        rs = calculate_relative_strength(data, nifty_data)
        previous_52_week_high = calculate_52_week_high(data)
        relative_volume = calculate_relative_volume(data)
        consolidation_percent , atr_percent = calculate_consolidation(data)
        data = calculate_adx(data)
        data = calculate_obv(data)

        #Market Structure
        swing_lows , swing_highs = find_swing_points(data ,window = SWING_WINDOW)
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
        
        scan_results = {
        "close": latest["Close"],
        "sma20": latest["ma20"],
        "sma50": latest["ma50"],
        "sma200": latest["ma200"],
        "adx": latest["adx"],
        "high_52w": previous_52_week_high,
        "market_structure": ( nearest_support is not None and
        nearest_resistance is not None),

        "obv_accumulation": latest["obv"] > data["obv"].iloc[-2],
        "macd_histogram": latest["macd_histogram"],
        "rsi": latest["rsi"],
        "atr_percent": atr_percent,
        }
        
        
        score_result = calculate_score(scan_results)
        score = score_result["score"]
        grade = score_result["grade"]
        percentage = score_result["percentage"]
        breakdown = score_result["breakdown"]
        
        #Printing Report
        stock_result = build_report(
        stock=stock,
        latest=latest,
        score_result=score_result,
        relative_strength=rs,
        previous_3_month_high=previous_3_month_high,
        previous_52_week_high=previous_52_week_high,
        todays_volume=todays_volume,
        avg_volume=avg_volume,
        relative_volume=relative_volume,
        consolidation_percent=consolidation_percent,
        atr_percent=atr_percent,
        nearest_support=nearest_support,
        nearest_resistance=nearest_resistance,
        support_distance=support_distance,
        resistance_distance=resistance_distance,)

        results.append(stock_result)



    except Exception as e:
        print(e)
        print(f"{stock} -> {e}")
        print(f"⚠️ Could not scan {stock}. Skipping...")
        continue

ranked_results = sort_results(results)

if OUTPUT_MODE == "full":

    for stock_result in ranked_results:
        print_report(stock_result)

elif OUTPUT_MODE == "summary":

    print_top_setups(ranked_results)
    print()
    print_market_summary(ranked_results)

else:

    raise ValueError(f"Invalid OUTPUT_MODE: {OUTPUT_MODE}")

print(f"ADX      : {latest['adx']:.2f}")
print(f"+DI      : {latest['plus_di']:.2f}")
print(f"-DI      : {latest['minus_di']:.2f}")
print(f"OBV      : {latest['obv']:,.0f}")