from config import (
    VOLUME_MULTIPLIER,
    CONSOLIDATION_MAX_RANGE_PERCENT,
    CONSOLIDATION_MAX_ATR_PERCENT,
    SCORING_WEIGHTS,
)

def get_rating(score):
    if score >= 90:
        return "⭐⭐⭐⭐⭐ Elite Swing Trade"
    elif score >= 75:
        return "⭐⭐⭐⭐☆ Strong Setup"
    elif score >= 60:
        return "⭐⭐⭐☆☆ Watchlist"
    elif score >= 40:
        return "⭐⭐☆☆☆ Average"
    return "⭐☆☆☆☆ Avoid"

def score_ma20(close, ma20):
    if close > ma20:
        return SCORING_WEIGHTS["ma20"], "Above 20 MA", None
    return 0, None, "Below 20 MA"


def score_ma50(close, ma50):
    if close > ma50:
        return SCORING_WEIGHTS["ma50"], "Above 50 MA", None
    return 0, None, "Below 50 MA"


def score_three_month_high(high, previous_high):
    if high > previous_high:
        return SCORING_WEIGHTS["three_month_high"], "3-Month High Breakout", None
    return 0, None, "No 3-Month High Breakout"


def score_relative_volume(relative_volume):
    if relative_volume >= 3:
        return (
            10,
            f"Exceptional Volume ({relative_volume:.2f}x)",
            None,)
    elif relative_volume >= 2:
        return (
            8,
            f"Excellent Volume ({relative_volume:.2f}x)",
            None,)
    elif relative_volume >= 1.5:
        return (
            6,
            f"Good Volume ({relative_volume:.2f}x)",
            None,)
    elif relative_volume >= VOLUME_MULTIPLIER:
        return (
            4,
            f"Above Average Volume ({relative_volume:.2f}x)",
            None,)
    return (
        0,
        None,
        f"Weak Volume ({relative_volume:.2f}x)",)


def score_rsi(rsi):
    if 55 <= rsi <= 65:
        return (
            5,
            f"Excellent RSI ({rsi:.1f})",
            None,)
    elif 50 <= rsi < 55:
        return (
            4,
            f"Healthy RSI ({rsi:.1f})",
            None,)
    elif 65 < rsi <= 70:
        return (
            4,
            f"Strong RSI ({rsi:.1f})",
            None,)
    elif 45 <= rsi < 50:
        return (
            2,
            f"Weak RSI ({rsi:.1f})",
            None,)
    elif 70 < rsi <= 75:
        return (
            2,
            f"RSI Slightly Overbought ({rsi:.1f})",
            None,)
    elif rsi > 75:
        return (
            0,
            None,
            f"RSI Overbought ({rsi:.1f})",)
    return (
        0,
        None,
        f"Weak RSI ({rsi:.1f})",)

def score_macd(macd, signal):
    if macd > signal:
        return SCORING_WEIGHTS["macd"], "Bullish MACD", None
    return 0, None, "Bearish MACD"


def score_relative_strength(rs):

    if rs is None:
        return (
            0,
            None,
            "Relative Strength Unavailable",)
    elif rs >= 5:
        return (
            15,
            f"Exceptional Relative Strength (+{rs:.2f}%)",
            None,)
    elif rs >= 2:
        return (
            10,
            f"Strong Relative Strength (+{rs:.2f}%)",
            None,)
    elif rs > 0:
        return (
            5,
            f"Positive Relative Strength (+{rs:.2f}%)",
            None,)
    return (
        0,
        None,
        f"Underperforming Nifty ({rs:.2f}%)",
    )


def score_52_week_high(high, previous_high):
    if high > previous_high:
        return SCORING_WEIGHTS["high_52_week"], "52-Week High Breakout", None
    return 0, None, "No 52-Week High Breakout"


def score_consolidation(consolidation_percent, atr_percent):
    if (
        consolidation_percent < CONSOLIDATION_MAX_RANGE_PERCENT
        and atr_percent < CONSOLIDATION_MAX_ATR_PERCENT
    ):
        return SCORING_WEIGHTS["consolidation"], "Tight Consolidation", None

    return 0, None, "No Consolidation"


def score_support(nearest_support, support_distance):

    if nearest_support is None or support_distance is None:
        return (
            0,
            None,
            "No Nearby Support",
        )

    strength = nearest_support["strength"]

    if strength == "Strong":

        if support_distance <= 2:
            return (
                10,
                f"Strong Support ({support_distance:.1f}% away)",
                None,
            )

        elif support_distance <= 5:
            return (
                8,
                f"Strong Support ({support_distance:.1f}% away)",
                None,
            )

    elif strength == "Medium":

        if support_distance <= 2:
            return (
                6,
                f"Medium Support ({support_distance:.1f}% away)",
                None,
            )

        elif support_distance <= 5:
            return (
                4,
                f"Medium Support ({support_distance:.1f}% away)",
                None,
            )

    return (
        0,
        None,
        "Weak/Far Support",
    )


def score_upside(nearest_resistance, resistance_distance):
    if nearest_resistance is None:
        return (
            10,
            "Clear Overhead (No Resistance Found)",
            None,)
    if resistance_distance is None:
        return (
            0,
            None,
            "Resistance Distance Unknown",)
    if resistance_distance >= 10:
        return (
            10,
            f"Excellent Upside ({resistance_distance:.1f}%)",
            None,)
    elif resistance_distance >= 5:
        return (
            8,
            f"Good Upside ({resistance_distance:.1f}%)",
            None,)
    elif resistance_distance >= 3:
        return (
            5,
            f"Limited Upside ({resistance_distance:.1f}%)",
            None,)
    return (
        0,
        None,
        f"Resistance Very Close ({resistance_distance:.1f}%)",
    )

def calculate_score(scan_results):
    trend_score = 0
    momentum_score = 0
    volume_score = 0
    structure_score = 0
    trade_quality_score = 0
    positive_signals = []
    negative_signals = []
    latest = scan_results["latest"]

    previous_3_month_high = scan_results["previous_3_month_high"]
    previous_52_week_high = scan_results["previous_52_week_high"]

    relative_volume = scan_results["relative_volume"]
    rs = scan_results["relative_strength"]

    consolidation_percent = scan_results["consolidation_percent"]
    atr_percent = scan_results["atr_percent"]

    nearest_support = scan_results["nearest_support"]
    support_distance = scan_results["support_distance"]

    nearest_resistance = scan_results["nearest_resistance"]
    resistance_distance = scan_results["resistance_distance"]


    # MA20
    points, success, failure = score_ma20(
    latest["Close"],
    latest["ma20"],)
    trend_score += points
    if success:
        positive_signals.append(success)
    if failure:
        negative_signals.append(failure)

    # MA50
    points, success, failure = score_ma50(
    latest["Close"],
    latest["ma50"],)
    trend_score += points
    if success:
        positive_signals.append(success)
    if failure:
        negative_signals.append(failure)

    # 3-Month High Breakout
    points, success, failure = score_three_month_high(
    latest["High"],
    previous_3_month_high,)
    trend_score += points
    if success:
        positive_signals.append(success)
    if failure:
        negative_signals.append(failure)

    # Relative Volume
    points, success, failure = score_relative_volume(
    relative_volume,)
    volume_score += points
    if success:
        positive_signals.append(success)
    if failure:
        negative_signals.append(failure)

    # RSI
    points, success, failure = score_rsi(
    latest["rsi"],)
    momentum_score += points
    if success:
        positive_signals.append(success)
    if failure:
        negative_signals.append(failure)

    # MACD
    points, success, failure = score_macd(
    latest["macd"],
    latest["signal"],)
    momentum_score += points
    if success:
        positive_signals.append(success)
    if failure:
        negative_signals.append(failure)

    # Relative Strength
    points, success, failure = score_relative_strength(rs,)
    momentum_score += points
    if success:
        positive_signals.append(success)
    if failure:
        negative_signals.append(failure)

    # 52-Week High Breakout
    points, success, failure = score_52_week_high(
    latest["High"],
    previous_52_week_high,)
    trend_score += points
    if success:
        positive_signals.append(success)
    if failure:
        negative_signals.append(failure)

    # Consolidation
    points, success, failure = score_consolidation(
    consolidation_percent,
    atr_percent,)
    structure_score += points
    if success:
        positive_signals.append(success)
    if failure:
        negative_signals.append(failure)

    # Market Structure

    # Strong Nearby Support
    points, success, failure = score_support(
    nearest_support,
    support_distance,)
    structure_score += points
    if success:
        positive_signals.append(success)
    if failure:
        negative_signals.append(failure)

    # Plenty of Upside
    points, success, failure = score_upside(
    nearest_resistance,
    resistance_distance,)
    trade_quality_score += points
    if success:
        positive_signals.append(success)
    if failure:
        negative_signals.append(failure)

    overall_score = (
    trend_score
    + momentum_score
    + volume_score
    + structure_score
    + trade_quality_score)

    rating = get_rating(overall_score)

    return {
    "score": overall_score,
    "trend_score": trend_score,
    "momentum_score": momentum_score,
    "volume_score": volume_score,
    "structure_score": structure_score,
    "trade_quality_score": trade_quality_score,
    "positive_signals": positive_signals,
    "negative_signals": negative_signals,
    "rating": rating,
}