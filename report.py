def build_report(
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
    trend_score,
    momentum_score,
    volume_score,
    structure_score,
    trade_quality_score,
):
    return {
        "ticker": stock,

        "score": score,
        "rating": rating,

        "latest": latest,

        "category_scores": {
            "trend": trend_score,
            "momentum": momentum_score,
            "volume": volume_score,
            "structure": structure_score,
            "trade_quality": trade_quality_score,
        },

        "trade": {
            "support": nearest_support,
            "resistance": nearest_resistance,
        },

        "signals": {
            "positive": positive_signals,
            "negative": negative_signals,
        },

        "analysis": {
            "relative_strength": rs,
            "previous_3_month_high": previous_3_month_high,
            "previous_52_week_high": previous_52_week_high,
            "todays_volume": todays_volume,
            "average_volume": avg_volume,
            "relative_volume": relative_volume,
            "consolidation_percent": consolidation_percent,
            "atr_percent": atr_percent,
            "support_distance": support_distance,
            "resistance_distance": resistance_distance,
        },
    }

def print_report(stock_result):
        
        stock = stock_result["ticker"]
        latest = stock_result["latest"]
        score = stock_result["score"]
        rating = stock_result["rating"]
        category_scores = stock_result["category_scores"]
        trade = stock_result["trade"]
        signals = stock_result["signals"]
        analysis = stock_result["analysis"]
        trend_score = category_scores["trend"]
        momentum_score = category_scores["momentum"]
        volume_score = category_scores["volume"]
        structure_score = category_scores["structure"]
        trade_quality_score = category_scores["trade_quality"]
        nearest_support = trade["support"]
        nearest_resistance = trade["resistance"]
        positive_signals = signals["positive"]
        negative_signals = signals["negative"]
        
        # -------------------- OUTPUT --------------------

        # ==========================
        # VERBOSE REPORT (Old Report)
        # Will be moved to print_verbose_report() in a future version.
        # ==========================
        # print("=" * 50)
        # print(f"{stock:^50}")
        # print("=" * 50)

        # print(f"{'Score':20}: {score}/100")
        # print(f"{'Rating':20}: {rating}")
        # print(f"{'Close':20}: {latest['Close']:.2f}")
        # print(f"{'MA20':20}: {latest['ma20']:.2f}")
        # print(f"{'MA50':20}: {latest['ma50']:.2f}")
        # print(f"{'RSI':20}: {latest['rsi']:.2f}")
        # print(f"{'ATR':20}: {latest['atr']:.2f}")
        # print(f"{'MACD':20}: {latest['macd']:.2f}")
        # print(f"{'MACD Signal':20}: {latest['signal']:.2f}")
        # print(f"{'Histogram':20}: {latest['histogram']:.2f}")

        # if rs is None:
        #     print(f"{'RS vs Nifty':20}: N/A")
        # else:
        #     print(f"{'RS vs Nifty':20}: {rs:.2f}%")

        # print("-" * 45)

        # print(f"{'Stop Loss':20}: {latest['stoploss']:.2f}")
        # print(f"{'Target':20}: {latest['target']:.2f}")
        # print(f"{'Risk':20}: {latest['risk']:.2f}")
        # print(f"{'Reward':20}: {latest['reward']:.2f}")
        # print(f"{'Reward : Risk':20}: {latest['rr']:.2f}")

        # print(f"{'Previous 3M High':20}: {previous_3_month_high:.2f}")
        # print(f"{'Previous 52W High':20}: {previous_52_week_high:.2f}")

        # print(f"{'Todays Volume':20}: {todays_volume:,.0f}")
        # print(f"{'20D Avg Volume':20}: {avg_volume:,.0f}")
        # print(f"{'Relative Volume':20}: {relative_volume:.2f}x")

        # print(f"{'Consolidation %':20}: {consolidation_percent:.2f}")
        # print(f"{'ATR %':20}: {atr_percent:.2f}")

        # print("---------------------------------------------")
        # print("Market Structure")

        # # Nearest Support
        # if nearest_support is not None:
        #     print(
        #         f"{'Nearest Support':25}: "
        #         f"{nearest_support['zone_low']:.2f} - "
        #         f"{nearest_support['zone_high']:.2f}"
        #     )
        #     print(
        #         f"{'Support Touches':25}: "
        #         f"{nearest_support['touches']}"
        #     )
        #     print(
        #         f"{'Support Strength':25}: "
        #         f"{nearest_support['strength']}"
        #     )
        #     print(
        #         f"{'Distance to Support':25}: "
        #         f"{support_distance:.2f}%"
        #     )
        # else:
        #     print(f"{'Nearest Support':25}: None")
        #     print(f"{'Support Touches':25}: -")
        #     print(f"{'Support Strength':25}: -")
        #     print(f"{'Distance to Support':25}: -")
                
        # # Nearest Resistance
        # if nearest_resistance is not None:
        #     print(
        #         f"{'Nearest Resistance':25}: "
        #         f"{nearest_resistance['zone_low']:.2f} - "
        #         f"{nearest_resistance['zone_high']:.2f}"
        #     )
        #     print(
        #         f"{'Resistance Touches':25}: "
        #         f"{nearest_resistance['touches']}"
        #     )
        #     print(
        #         f"{'Resistance Strength':25}: "
        #         f"{nearest_resistance['strength']}"
        #     )

        #     print(
        #     f"{'Distance to Resistance':25}:"
        #     f"{resistance_distance: .2f}%"
        #     )
        # else:
        #     print(f"{'Nearest Resistance':25}: None")
        #     print(f"{'Resistance Touches':25}: -")
        #     print(f"{'Resistance Strength':25}: -")
        #     print(f"{'Distance to Resistance':25}: -")

        # print("-" * 45)
        # print()

        # print("Trading Signals:")
        # for signal in positive_signals:
        #     print(f"✅ {signal}")
        # for signal in negative_signals:
        #     print(f"❌ {signal}")

        print("=" * 50)
        print(f"{stock:^50}")
        print("=" * 50)
        print()

        # Overall Score
        print("Overall Score")
        print("-" * 13)
        print(f"{score} / 100")
        print(rating)
        print()

        # Category Scores
        print("Category Scores")
        print("-" * 15)
        print(f"{'Trend':20}: {min(trend_score, 30)} / 30")
        print(f"{'Momentum':20}: {min(momentum_score, 20)} / 20")
        print(f"{'Volume':20}: {min(volume_score, 20)} / 20")
        print(f"{'Structure':20}: {min(structure_score, 15)} / 15")
        print(f"{'Trade Quality':20}: {min(trade_quality_score, 15)} / 15")
        print()

        # Trade
        print("Trade")
        print("-" * 5)
        print(f"{'Current Price':20}: {latest['Close']:.2f}")

        if nearest_support:
            print(
                f"{'Support':20}: "
                f"{nearest_support['zone_low']:.2f} - "
                f"{nearest_support['zone_high']:.2f}"
            )
        else:
            print(f"{'Support':20}: None")

        if nearest_resistance:
            print(
                f"{'Resistance':20}: "
                f"{nearest_resistance['zone_low']:.2f} - "
                f"{nearest_resistance['zone_high']:.2f}"
            )
        else:
            print(f"{'Resistance':20}: None")

        print(f"{'Reward : Risk':20}: 1 : {latest['rr']:.2f}")
        print()

        # Highlights
        print("Highlights")
        print("-" * 10)

        if positive_signals:
            for signal in positive_signals:
                print(f"✅ {signal}")
        else:
            print("None")

        print()

        # Weaknesses
        print("Weaknesses")
        print("-" * 10)

        if negative_signals:
            for signal in negative_signals:
                print(f"❌ {signal}")
        else:
            print("None")

        print()
        print("=" * 50)
        print()

def print_top_setups(results, top_n=10):

    print("=" * 60)
    print(f"{'TOP 10 SWING SETUPS':^60}")
    print("=" * 60)
    print()

    print(f"{'Rank':<6}{'Ticker':<20}{'Score':<10}{'Rating'}")
    print("-" * 60)
  

    for rank, stock in enumerate(results[:top_n], start=1):
        print(
            f"{rank:<6}"
            f"{stock['ticker']:<20}"
            f"{stock['score']:<10}"
            f"{stock['rating']}"
        )

    print()



def print_market_summary(results):

    elite = 0
    strong = 0
    watchlist = 0
    average = 0
    avoid = 0

    for stock in results:

        rating = stock["rating"]

        if "Elite" in rating:
            elite += 1

        elif "Strong" in rating:
            strong += 1

        elif "Watchlist" in rating:
            watchlist += 1

        elif "Average" in rating:
            average += 1

        elif "Avoid" in rating:
            avoid += 1

    print("=" * 60)
    print(f"{'MARKET SUMMARY':^60}")
    print("=" * 60)
    print()

    print(f"{'Stocks Scanned':25}: {len(results)}")
    print(f"{'Elite Setups':25}: {elite}")
    print(f"{'Strong Setups':25}: {strong}")
    print(f"{'Watchlist':25}: {watchlist}")
    print(f"{'Average':25}: {average}")
    print(f"{'Avoid':25}: {avoid}")
    print()