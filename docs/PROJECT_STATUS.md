# 📗 PROJECT_STATUS

# Swing Scanner

**Current Version:** **2.2**

**Project Status:** 🟢 Active Development

---

# Overview

The Swing Scanner is a Python-based swing trading scanner built while learning Python from scratch.

The project downloads live NSE stock data, calculates multiple technical indicators, evaluates swing trading conditions, generates trade plans, and assigns a swing score to each stock.

The project focuses on writing clean, modular, and maintainable code while gradually learning software engineering principles.

---

# Completed Features

## Core

* Live Yahoo Finance data
* CSV Watchlist
* Error Handling
* Modular Architecture
* Professional Console Output

---

## Technical Indicators

* 20-Day Moving Average (MA20)
* 50-Day Moving Average (MA50)
* RSI
* ATR
* MACD
* MACD Signal Line
* MACD Histogram
* Relative Strength vs Nifty
* Relative Volume (RVOL)

---

## Breakout Detection

* Previous 3-Month High
* Previous 52-Week High

---

## Trade Planning

* Stop Loss
* Target
* Risk
* Reward
* Reward : Risk Ratio

---

## Scanner

* 8-Point Swing Scoring System
* Trading Signals
* Breakout Detection
* Relative Strength Analysis
* Relative Volume Confirmation

---

# Current Project Structure

```text
Swing-Scanner/
│
├── data/
│   └── stocks.csv
├── docs/
│   ├── LEARNING_LOG.md
│   ├── PROJECT_STATUS.md
│   └── ROADMAP.md
├── reports/
├── indicators.py
├── scanner.py
├── stockanalysis.py
├── live_data.py
├── pandasbasics.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Current Strengths

* Clean modular architecture
* Reusable indicator functions
* Professional console output
* Consistent naming conventions
* Good code readability
* Live market data integration
* Risk management calculations
* Multiple technical indicators
* Structured Git workflow

---

# Current Limitations

The scanner currently does **not** include:

* Consolidation Detection
* Support & Resistance
* Automatic CSV Reports
* Ranked Results
* Portfolio Scanner
* Streamlit Dashboard
* Charts
* Telegram Alerts
* AI-based Trade Explanations

---

# Next Milestone

## Version 2.3

### Planned Feature

* Consolidation Detection

This feature will identify stocks trading in a tight price range before a potential breakout, improving the quality of swing trade opportunities detected by the scanner.

---

# Development Workflow

Every version follows the same workflow:

Feature Development

↓

Cleanup & Refactoring

↓

Testing

↓

Documentation Update

↓

Git Commit

↓

Git Push

---

# Overall Progress

Project Foundation

* ✅ Completed

Technical Indicators

* ✅ Completed (Current Scope)

Breakout Detection

* ✅ Completed (Current Scope)

Trade Planning

* ✅ Completed

Scanner Logic

* ✅ Completed

Documentation

* ✅ Maintained

Future Enhancements

* 🚧 In Progress
