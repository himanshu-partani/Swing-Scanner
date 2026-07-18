"""
==========================================================
Swing Scanner V4.0 Configuration
==========================================================

Central configuration for:

• Data Settings
• Indicator Parameters
• Market Structure
• Scoring Engine
• Scanner Filters

Changing values here automatically updates the
entire scanner.
"""

# ==========================================================
# DATA SETTINGS
# ==========================================================

LOOKBACK_3_MONTHS = 63
LOOKBACK_52_WEEKS = 252
LOOKBACK_52W = 252
# Maximum distance from 52-week high (%)
HIGH_52W_DISTANCE = 10

# ==========================================================
# MARKET DATA
# ==========================================================

MARKET_INDEX = "^NSEI"

DATA_PERIOD = "13mo"
DATA_INTERVAL = "1d"

# ==========================================================
# BACKWARD COMPATIBILITY
# ==========================================================

DOWNLOAD_PERIOD = DATA_PERIOD
DOWNLOAD_INTERVAL = DATA_INTERVAL

# ==========================================================
# FILES
# ==========================================================

WATCHLIST_FILE = "data/stocks.csv"
NIFTY500_FILE = "data/nifty500.csv"

# ==========================================================
# MOVING AVERAGES
# ==========================================================

MA20_PERIOD = 20
MA50_PERIOD = 50
MA200_PERIOD = 200

# ==========================================================
# RSI
# ==========================================================

RSI_PERIOD = 14

# ==========================================================
# ATR
# ==========================================================

ATR_PERIOD = 14
RSI_MIN = 50
RSI_MAX = 70

# ATR penalty threshold (% of current price)
ATR_PENALTY_THRESHOLD = 5.0

# ==========================================================
# ADX
# ==========================================================

ADX_PERIOD = 14

ADX_WEAK = 20
ADX_STRONG = 25
ADX_VERY_STRONG = 35
ADX_EXTREME = 45
# Minimum ADX required for scoring
ADX_THRESHOLD = 25
# ==========================================================
# MACD
# ==========================================================

MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9

# ==========================================================
# VOLUME
# ==========================================================

VOLUME_MULTIPLIER = 1.20

# ==========================================================
# CONSOLIDATION
# ==========================================================

CONSOLIDATION_MAX_RANGE_PERCENT = 5
CONSOLIDATION_MAX_ATR_PERCENT = 2

# ==========================================================
# MARKET STRUCTURE
# ==========================================================

SWING_WINDOW = 5

ZONE_THRESHOLD = 2
ZONE_THRESHOLD_PERCENT = 2

SUPPLY_DEMAND_MIN_TOUCHES = 2
MIN_TOUCHES = 2
MIN_SUPPORT_TOUCHES = 2
MIN_RESISTANCE_TOUCHES = 2


# ==========================================================
# SCORING ENGINE
# ==========================================================

SCORE_WEIGHTS = {
    "Trend": 20,
    "ADX": 18,
    "52W High": 16,
    "Multi Timeframe": 15,
    "Market Structure": 12,
    "OBV": 9,
    "MACD": 4,
    "RSI": 2,
    "ATR Bonus": 4,
}

# ==========================================================
# RATING
# ==========================================================

GRADE_THRESHOLDS = {
    "A+": 90,
    "A": 75,
    "B": 60,
    "C": 40,
}

# ==========================================================
# DEBUG
# ==========================================================

DEBUG_MODE = False

SCAN_MODE = "nifty500"
OUTPUT_MODE = "summary"