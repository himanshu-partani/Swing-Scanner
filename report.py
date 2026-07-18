"""
Swing Scanner V4.0 - report.py
Compatible with the V4 scoring engine.
"""

def build_report(
    stock,
    latest,
    score_result,
    relative_strength,
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
):
    
    return {
        "ticker": stock,
        "latest": latest,
        "score": score_result["score"],
        "grade": score_result["grade"],
        "percentage": score_result["percentage"],
        "breakdown": score_result["breakdown"],
        "trade": {
            "support": nearest_support,
            "resistance": nearest_resistance,
        },
        "analysis": {
            "relative_strength": relative_strength,
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
    latest = stock_result["latest"]
    trade = stock_result["trade"]
    analysis = stock_result["analysis"]

    print("=" * 60)
    print(f'{stock_result["ticker"]:^60}')
    print("=" * 60)
    print(f'Score      : {stock_result["score"]}/100')
    print(f'Grade      : {stock_result["grade"]}')
    print(f'Percentage : {stock_result["percentage"]:.1f}%')
    print()
    print("Breakdown")
    print("-" * 60)
    for name, value in stock_result["breakdown"].items():
        print(f"{name:35}: {value}")
    print()
    print("Trade")
    print("-" * 60)
    print(f'Current Price : {latest["Close"]:.2f}')
    if trade["support"]:
        s = trade["support"]
        print(f'Support      : {s["zone_low"]:.2f} - {s["zone_high"]:.2f}')
    else:
        print("Support      : None")
    if trade["resistance"]:
        r = trade["resistance"]
        print(f'Resistance   : {r["zone_low"]:.2f} - {r["zone_high"]:.2f}')
    else:
        print("Resistance   : None")
    print(f'Reward:Risk  : 1 : {latest["rr"]:.2f}')
    print()
    print("Technical")
    print("-" * 60)
    print(f'RSI               : {latest["rsi"]:.2f}')
    print(f'ADX               : {latest.get("adx","N/A")}')
    print(f'ATR               : {latest["atr"]:.2f}')
    print(f'MACD Histogram    : {latest.get("macd_histogram",0):.2f}')
    rs = analysis["relative_strength"]
    print(f'Relative Strength : {"N/A" if rs is None else f"{rs:.2f}%"}')
    print(f'Relative Volume   : {analysis["relative_volume"]:.2f}x')
    print("=" * 60)


def print_top_setups(results, top_n=10):
    print("=" * 60)
    print(f'{"TOP SWING SETUPS":^60}')
    print("=" * 60)
    print(f'{"Rank":<6}{"Ticker":<20}{"Score":<10}Grade')
    print("-"*60)
    for i, stock in enumerate(results[:top_n],1):
        print(f'{i:<6}{stock["ticker"]:<20}{stock["score"]:<10}{stock["grade"]}')


def print_market_summary(results):
    grades = {"A+":0,"A":0,"B":0,"C":0,"D":0}
    for stock in results:
        g = stock.get("grade","D")
        if g in grades:
            grades[g]+=1
        else:
            grades["D"]+=1
    print("="*60)
    print(f'{"MARKET SUMMARY":^60}')
    print("="*60)
    print(f'Stocks Scanned : {len(results)}')
    for g,v in grades.items():
        print(f'{g:<15}: {v}')
