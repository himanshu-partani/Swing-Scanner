# 🚀 Swing Scanner v3.1

> A professional Python-based Swing Trading Scanner that analyzes NSE stocks using technical analysis, market structure, and a rule-based scoring system to identify high-quality swing trading opportunities.

---

# 📌 Overview

Swing Scanner is a modular Python project built to automate swing trade analysis for Indian stocks.

Instead of manually checking dozens of charts every day, the scanner evaluates multiple technical conditions, calculates a quality score, identifies important support and resistance zones, and presents everything in a clean, readable console output.

The project has been built incrementally as a learning journey—from basic Python programming to designing a modular technical analysis engine.

Current Version: **v3.1**

---

# ✨ Features

## 📊 Technical Indicators

- ✅ 20-Day Moving Average (MA20)
- ✅ 50-Day Moving Average (MA50)
- ✅ Relative Strength Index (RSI)
- ✅ Average True Range (ATR)
- ✅ MACD
- ✅ Relative Strength vs NIFTY
- ✅ Relative Volume
- ✅ Previous 3-Month High Detection
- ✅ 52-Week High Detection
- ✅ Tight Consolidation Detection

---

## 📈 Market Structure Engine

Version 3 introduced a dedicated market structure module.

Features include:

- Swing High Detection
- Swing Low Detection
- Price Zone Grouping
- Zone Strength Classification
- Strong/Weak Support Identification
- Strong/Weak Resistance Identification
- Distance to Support
- Distance to Resistance
- Professional Zone Filtering

---

## 🎯 Rule-Based Scoring System

Every stock is evaluated against predefined trading conditions.

The scanner assigns points for bullish characteristics including:

- Above MA20
- Above MA50
- RSI in healthy range
- MACD Bullish
- Relative Strength Positive
- Volume Breakout
- Previous 3-Month High
- Near 52-Week High
- Tight Consolidation
- Additional market structure confirmations

The final score allows quick ranking of trading opportunities.

---

## 📋 Professional Console Output

For every stock, the scanner displays:

- Current Price
- Moving Averages
- RSI
- ATR
- MACD
- Relative Strength
- Relative Volume
- Previous 3-Month High
- 52-Week High Status
- Consolidation Status
- Support Levels
- Resistance Levels
- Distance to Support
- Distance to Resistance
- Individual Signal Status
- Overall Score

---

# 🏗 Architecture

Version 3.1 follows a modular architecture.

```
scanner.py
│
├── Downloads market data
├── Calculates indicators
├── Calculates market structure
├── Evaluates trading rules
├── Calculates score
└── Prints final report

indicators.py
│
├── RSI
├── ATR
├── MACD
├── Relative Strength
├── Relative Volume
├── Moving Averages
├── Consolidation
├── 52 Week High
└── Trading indicators

market_structure.py
│
├── Swing Point Detection
├── Zone Grouping
├── Zone Filtering
├── Zone Strength
└── Nearest Support & Resistance
```

Each module has a single responsibility, making the project easier to maintain, test, and extend.

---

# 📂 Project Structure

```
Swing-Scanner/
│
├── data/
│   └── stocks.csv
│
├── docs/
│   ├── LEARNING_LOG.md
│   ├── PROJECT_STATUS.md
│   └── ROADMAP.md
│
├── indicators.py
├── market_structure.py
├── scanner.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Swing-Scanner.git
```

Move into the project:

```bash
cd Swing-Scanner
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 📄 Configure Watchlist

Edit:

```
data/stocks.csv
```

Example:

```csv
Ticker
RELIANCE.NS
SBIN.NS
TCS.NS
HCLTECH.NS
ANGELONE.NS
```

---

# ▶ Usage

Run:

```bash
python scanner.py
```

The scanner will:

1. Download market data
2. Calculate indicators
3. Analyze market structure
4. Evaluate trading rules
5. Generate scores
6. Print a complete report for every stock

---

# 🏆 Scoring System

The scanner uses a rule-based scoring model.

Each bullish condition contributes one point toward the final score.

Typical confirmations include:

- ✅ Price above MA20
- ✅ Price above MA50
- ✅ RSI in bullish range
- ✅ MACD Bullish
- ✅ Relative Strength Positive
- ✅ Relative Volume Breakout
- ✅ Previous 3-Month High
- ✅ Near 52-Week High
- ✅ Tight Consolidation
- ✅ Market Structure Confirmation

Higher scores indicate stronger swing trading setups.

The scoring system is intentionally transparent and easy to modify as the project evolves.

---

# 🧠 Technologies Used

- Python
- Pandas
- NumPy
- yfinance
- Git
- GitHub

---

# ⭐ Version 3.1 Highlights

Version 3.1 focused on improving code quality, maintainability, and documentation while preserving the existing trading logic.

### Improvements

- Professional project documentation
- Cleaner code organization
- Improved project structure
- Better developer experience
- Updated repository documentation
- Refined console output formatting
- Consistent project standards
- Architecture cleanup

Version 3.1 is a stability and refinement release that prepares the project for future feature development.

---

# 🛣 Roadmap Summary

### ✅ Completed

- Multi-stock scanning
- Moving averages
- RSI
- ATR
- MACD
- Relative Strength
- Relative Volume
- Previous 3-Month High
- 52-Week High
- Tight Consolidation
- Market Structure Engine
- Support & Resistance Detection
- Modular architecture
- Rule-based scoring system

---

### 🚧 Planned

- NIFTY 500 Scanner
- Automatic Stock Ranking
- CSV Report Generation
- Portfolio Scanner
- Interactive Charts
- Streamlit Dashboard
- Telegram Alerts
- AI Trade Explanations
- Portfolio Analytics
- Advanced Screening Filters
- Performance Optimization

---

# 🔮 Future Plans

The long-term vision for Swing Scanner is to evolve from a command-line technical analysis tool into a complete swing trading platform.

Future development will focus on:

- Faster scanning
- Better ranking algorithms
- Portfolio management
- Interactive visualizations
- AI-assisted trade analysis
- Web dashboard
- Automated notifications
- Historical backtesting
- Performance analytics
- Production-ready architecture

---

# 📚 Learning Goals

This project is also a structured software engineering journey.

Key areas explored include:

- Python Programming
- Modular Design
- Technical Analysis
- Financial Data Processing
- Algorithm Design
- Market Structure Analysis
- Git & GitHub
- Software Documentation
- Clean Code Principles
- Project Architecture

---

# 🤝 Contributing

Suggestions, improvements, and feedback are always welcome.

Feel free to fork the project, experiment with new ideas, and submit improvements.

---

# 📄 License

This project is intended for educational purposes.

Always perform your own research before making investment decisions. The scanner provides technical analysis and should not be considered financial advice.

---

# 🚀 Swing Scanner v3.1

Professional • Modular • Educational • Built for Continuous Improvement