"""
=========================================================
Swing Scanner V4.0
Production Scoring Engine
=========================================================

Research-backed weighted scoring engine.

Scoring Matrix
--------------

Trend...................................22
ADX.....................................20
52W High Distance.......................16
20 > 50 > 200 Alignment.................16
Higher High Higher Low..................12
OBV Accumulation........................10
MACD Histogram.......................... 4
RSI..................................... 2
ATR Expansion...........................10

Maximum Score : 100

Author : Swing Scanner
Version : 4.0
"""

from __future__ import annotations
from typing import Any, Dict


from config import (
    SCORE_WEIGHTS,
    GRADE_THRESHOLDS,
    ADX_THRESHOLD,
    RSI_MIN,
    RSI_MAX,
    HIGH_52W_DISTANCE,
    ATR_PENALTY_THRESHOLD,
)


# ==========================================================
# Helper Functions
# ==========================================================

def bool_score(condition: bool, weight: int) -> int:
    """
    Returns weight if condition is True.
    """

    return weight if condition else 0


def calculate_grade(score_percent: float) -> str:
    """
    Convert percentage score into grade.
    """
    if score_percent >= GRADE_THRESHOLDS["A+"]:
        return "A+"

    if score_percent >= GRADE_THRESHOLDS["A"]:
        return "A"

    if score_percent >= GRADE_THRESHOLDS["B"]:
        return "B"

    if score_percent >= GRADE_THRESHOLDS["C"]:
        return "C"

    return "D"

# ==========================================================
# Validation
# ==========================================================

REQUIRED_FIELDS = (
    "close",
    "sma20",
    "sma50",
    "sma200",
    "adx",
    "high_52w",
    "market_structure",
    "obv_accumulation",
    "macd_histogram",
    "rsi",
    "atr_percent",
)


def validate_stock(stock: Dict[str, Any]) -> None:
    """
    Ensure all required values exist before scoring.
    """

    missing = [
        field
        for field in REQUIRED_FIELDS
        if field not in stock
    ]

    if missing:
        raise KeyError(
            f"Missing scoring fields: {', '.join(missing)}"
        )


# ==========================================================
# Individual Scoring Functions
# ==========================================================

def score_trend(stock: Dict[str, Any]) -> int:
    """
    Close above 200 SMA
    """

    return bool_score(
        stock["close"] > stock["sma200"],
        SCORE_WEIGHTS["Trend"],
    )


def score_adx(stock: Dict[str, Any]) -> int:
    """
    ADX Trend Strength
    """

    return bool_score(
        stock["adx"] >= ADX_THRESHOLD,
        SCORE_WEIGHTS["ADX"],
    )


def score_52_week_high(stock: Dict[str, Any]) -> int:
    """
    Stock trading within configured %
    of 52 Week High.
    """

    high = stock["high_52w"]

    if high <= 0:
        return 0

    distance = (
        (high - stock["close"])
        / high
    ) * 100

    return bool_score(
        distance <= HIGH_52W_DISTANCE,
        SCORE_WEIGHTS["52W High"],
    )


def score_multi_timeframe(stock: Dict[str, Any]) -> int:
    """
    20 > 50 > 200 SMA Alignment
    """

    sma20 = stock["sma20"]
    sma50 = stock["sma50"]
    sma200 = stock["sma200"]

    condition = sma20 > sma50 > sma200

    return bool_score(
        condition,
        SCORE_WEIGHTS["Multi Timeframe"],
    )

# ==========================================================
# Market Structure
# ==========================================================

def score_market_structure(stock: Dict[str, Any]) -> int:
    """
    Higher High + Higher Low structure.
    """

    return bool_score(
        stock["market_structure"],
        SCORE_WEIGHTS["Market Structure"],
    )


# ==========================================================
# OBV
# ==========================================================

def score_obv(stock: Dict[str, Any]) -> int:
    """
    Positive OBV accumulation.
    """

    return bool_score(
        stock["obv_accumulation"],
        SCORE_WEIGHTS["OBV"],
    )


# ==========================================================
# MACD
# ==========================================================

def score_macd(stock: Dict[str, Any]) -> int:
    """
    Positive MACD Histogram.
    """

    return bool_score(
        stock["macd_histogram"] > 0,
        SCORE_WEIGHTS["MACD"],
    )


# ==========================================================
# RSI
# ==========================================================

def score_rsi(stock: Dict[str, Any]) -> int:
    """
    Healthy RSI range.
    """

    rsi = max(0, min(100, stock["rsi"]))

    return bool_score(
        RSI_MIN <= rsi <= RSI_MAX,
        SCORE_WEIGHTS["RSI"],
    )


# ==========================================================
# ATR Bonus
# ==========================================================

def score_atr_bonus(stock: Dict[str, Any]) -> int:
    """
    Reward expanding volatility.
    Backtesting across the NIFTY 500 showed that
    stocks with ATR% above the threshold produced
    stronger forward returns than low-volatility stocks.
    Research showed ATR > threshold
    had significantly better forward returns.
    """

    if stock["atr_percent"] > ATR_PENALTY_THRESHOLD:
        return SCORE_WEIGHTS["ATR Bonus"]
    else:

        return 0

# ==========================================================
# Score Breakdown
# ==========================================================

def build_breakdown(stock: Dict[str, Any]) -> Dict[str, int]:
    """
    Evaluate every scoring factor independently.
    """

    breakdown = {

        "Trend":
            score_trend(stock),

        "ADX":
            score_adx(stock),

        "52W High":
            score_52_week_high(stock),

        "Multi Timeframe":
            score_multi_timeframe(stock),

        "Market Structure":
            score_market_structure(stock),

        "OBV":
            score_obv(stock),

        "MACD":
            score_macd(stock),

        "RSI":
            score_rsi(stock),

        "ATR Bonus":
            score_atr_bonus(stock),
    }

    return breakdown

# ==========================================================
# Main Scoring Engine
# ==========================================================

def calculate_score(stock: Dict[str, Any]) -> Dict[str, any]:
    """
    Calculate the complete Swing Scanner V4.0 score.

    Parameters
    ----------
    stock : dict
        Dictionary containing all calculated indicators.

    Returns
    -------
    dict
        {
            "score": int,
            "max_score": int,
            "percentage": float,
            "grade": str,
            "breakdown": dict
        }
    """
    validate_stock(stock)
    breakdown = build_breakdown(stock)

    total_score = sum(breakdown.values())

    # Maximum achievable score ignores penalties.
    max_score = sum(SCORE_WEIGHTS.values())


    score_percentage = round(
    (total_score / max_score) * 100,
    2,
)

    grade = calculate_grade(score_percentage)

    return {
        "score": total_score,
        "max_score": max_score,
        "percentage": score_percentage,
        "grade": grade,
        "breakdown": breakdown,
    }


# ==========================================================
# Console Debug Helper
# ==========================================================

def print_score_breakdown(result: Dict[str, Any]) -> None:
    """
    Pretty-print the score breakdown.

    Useful while debugging or testing.
    """

    print()
    print("=" * 55)
    print("SWING SCANNER V4.0 SCORE BREAKDOWN")
    print("=" * 55)

    for factor, score in result["breakdown"].items():
        print(f"{factor:<25} {score:>5}")

    print("-" * 55)

    print(
        f"{'TOTAL SCORE':<25}"
        f"{result['score']} / {result['max_score']}"
    )

    print(
        f"{'PERCENTAGE':<25}"
        f"{result['percentage']}%"
    )

    print(
        f"{'GRADE':<25}"
        f"{result['grade']}"
    )

    print("=" * 55)
    print()


# ==========================================================
# End of File
# ==========================================================

__all__ = [
    "calculate_score",
    "print_score_breakdown",
]