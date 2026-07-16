from report import print_report
from data_loader import (
    load_watchlist,
    download_nifty_data,
    download_market_data,
)

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

from config import (
    LOOKBACK_3_MONTHS,
    VOLUME_MULTIPLIER,
    CONSOLIDATION_MAX_RANGE_PERCENT,
    CONSOLIDATION_MAX_ATR_PERCENT,
    MIN_SUPPORT_TOUCHES,
    MIN_RESISTANCE_TOUCHES,
)

# Download Nifty data once
nifty_data = download_nifty_data()

# Read watchlist
stocks = load_watchlist()

market_data = download_market_data(stocks)

for stock in stocks:
    try:
        data = market_data[stock]

        if data.empty:
            print(f"⚠️ {stock} returned no data. Skipping...")
            continue

        current_price = float(data["Close"].iloc[-1])
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
        
        scan_results = {
            "latest": latest,
            "previous_3_month_high": previous_3_month_high,
            "previous_52_week_high": previous_52_week_high,
            "relative_volume": relative_volume,
            "relative_strength": rs,
            "consolidation_percent": consolidation_percent,
            "atr_percent": atr_percent,
            "nearest_support": nearest_support,
            "support_distance": support_distance,
            "nearest_resistance": nearest_resistance,
            "resistance_distance": resistance_distance,}
        
        from scoring import calculate_score
        from scoring import get_rating
        score_result = calculate_score(scan_results)
        score = score_result["score"]
        rating = get_rating(score)
        positive_signals = score_result["positive_signals"]
        negative_signals = score_result["negative_signals"]
        
        
        #Printing Report
        print_report(
        stock,
        latest,
        score,
        rs,
        previous_3_month_high,
        previous_52_week_high,
        todays_volume,
        avg_volume,
        relative_volume,
        consolidation_percent,
        atr_percent,
        nearest_support,
        nearest_resistance,
        support_distance,
        resistance_distance,
        positive_signals,
        negative_signals,
        rating,
         score_result["trend_score"],
        score_result["momentum_score"],
        score_result["volume_score"],
        score_result["structure_score"],
        score_result["trade_quality_score"],
        )



    except Exception as e:
        print(e)
        print(f"⚠️ Could not scan {stock}. Skipping...")
        continue