# =====================================
# Download Settings
# =====================================

LOOKBACK_3_MONTHS = 63


# =====================================
# Indicator Settings
# =====================================

VOLUME_MULTIPLIER = 1.2
CONSOLIDATION_MAX_RANGE_PERCENT = 5
CONSOLIDATION_MAX_ATR_PERCENT = 2


# =====================================
# Market Structure Settings
# =====================================

MIN_SUPPORT_TOUCHES = 2
MIN_RESISTANCE_TOUCHES = 2


# =====================================
# Data Settings
# =====================================

WATCHLIST_FILE = "data/stocks.csv"
MARKET_INDEX = "^NSEI"
DOWNLOAD_PERIOD = "13mo"

SCORING_WEIGHTS = {
    "ma20": 5,
    "ma50": 5,
    "three_month_high": 10,
    "high_52_week": 15,
    "relative_volume": 10,
    "rsi": 5,
    "macd": 5,
    "relative_strength": 15,
    "consolidation": 10,
    "support": 10,
    "upside": 10,
}

# ==========================
# Scan Configuration
# ==========================

SCAN_MODE = "nifty500"

# Options:
# "watchlist"
# "nifty500"

# ==========================
# Output Configuration
# ==========================

OUTPUT_MODE = "summary"

# Options:
# "full"
# "summary"


