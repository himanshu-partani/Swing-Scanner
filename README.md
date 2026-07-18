# 🚀 Swing Scanner

> **A Modular Quantitative Swing Trading Scanner for the Indian Stock Market**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Latest-green.svg)
![Yahoo Finance](https://img.shields.io/badge/Data-Yahoo%20Finance-orange.svg)
![Version](https://img.shields.io/badge/Version-4.0-success.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

---

# Overview

Swing Scanner is a modular Python application that identifies high-quality swing trading opportunities in the Indian stock market using technical analysis, market structure, and a professional weighted scoring engine.

Originally started as a Python learning journey, the project has evolved into a structured software engineering application featuring clean architecture, reusable modules, centralized configuration, batch data processing, and a scalable analysis pipeline capable of scanning the complete NIFTY 500 universe.

**Version 4.0** represents the first production-ready release of the scanner.

---

# Features

## 📊 Market Data

- Live market data from Yahoo Finance
- Batch download engine
- Personal watchlist scanning
- Complete NIFTY 500 scanning
- Automatic NIFTY benchmark download

---

## 📈 Technical Analysis

- SMA20
- SMA50
- SMA200
- RSI
- ATR
- ADX (+DI / −DI)
- MACD
- OBV (On Balance Volume)
- Relative Strength vs NIFTY
- Relative Volume
- Previous 3-Month High
- 52-Week High Proximity

---

## 🏗 Market Structure Engine

- Swing Point Detection
- Support Zone Detection
- Resistance Zone Detection
- Zone Grouping
- Zone Strength Classification
- Nearest Support Detection
- Nearest Resistance Detection
- Distance Calculations

---

## 🎯 Professional Scoring Engine

The Version 4.0 scoring engine evaluates multiple independent technical factors to generate a weighted composite score.

### Current Scoring Factors

- Long-Term Trend
- Multi-Timeframe Alignment
- ADX Trend Strength
- Market Structure
- 52-Week High Proximity
- OBV
- MACD
- RSI
- ATR Bonus

Every stock receives:

- Numerical Score
- Percentage Score
- Letter Grade
- Market Ranking

### Grade System

| Grade | Score |
|--------|------:|
| A+ | 90 – 100 |
| A | 75 – 89 |
| B | 60 – 74 |
| C | 40 – 59 |
| D | Below 40 |

---

# Reporting System

Two reporting modes are available.

## Full Mode

Displays detailed analysis for every scanned stock including:

- Technical indicators
- Individual scoring factors
- Market structure
- Final score
- Letter grade

---

## Summary Mode

Displays:

- Top Swing Setups
- Market Summary
- Grade Distribution

Designed for large scans such as the NIFTY 500.

---

# Example Output

```text
============================================================
                      TOP SWING SETUPS
============================================================

Rank   Ticker              Score   Grade

1      PNBHOUSING.NS       96      A+
2      INDUSINDBK.NS       94      A+
3      RAINBOW.NS          94      A+
...

============================================================
                      MARKET SUMMARY
============================================================

Stocks Scanned : 500

A+ : 13
A  : 60
B  : 89
C  : 96
D  : 242
```

---

# Project Structure

```text
Swing-Scanner
│
├── config.py
├── data_loader.py
├── indicators.py
├── market_structure.py
├── scoring.py
├── ranking.py
├── report.py
├── scanner.py
│
├── tools/
│   └── prepare_nifty500.py
│
├── data/
│   ├── stocks.csv
│   ├── nifty500.csv
│   └── official_nifty500.csv
│
├── docs/
│   ├── LEARNING_LOG.md
│   ├── PROJECT_STATUS.md
│   └── ROADMAP.md
│
└── README.md
```

---

# Architecture

```text
                 config.py
                      │
                      ▼
              data_loader.py
                      │
                      ▼
                indicators.py
                      │
                      ▼
           market_structure.py
                      │
                      ▼
                 scoring.py
                      │
                      ▼
                 ranking.py
                      │
                      ▼
                  report.py
                      │
                      ▼
                 scanner.py
```

---

# Installation

Clone the repository.

```bash
git clone https://github.com/yourusername/Swing-Scanner.git
```

Enter the project directory.

```bash
cd Swing-Scanner
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the scanner.

```bash
python scanner.py
```

---

# Configuration

All project settings are centralized inside:

```text
config.py
```

Examples:

```python
SCAN_MODE = "watchlist"
OUTPUT_MODE = "summary"
```

Additional configurable parameters include:

- Indicator periods
- Scoring weights
- Download settings
- Market structure thresholds
- Scanner options

---

# Scan Modes

## Watchlist Mode

Scans stocks listed inside:

```text
data/stocks.csv
```

Ideal for personal watchlists.

---

## NIFTY 500 Mode

Scans the complete NIFTY 500 universe.

Prepare the ticker list using:

```bash
python tools/prepare_nifty500.py
```

---

# Software Design

Swing Scanner follows a modular architecture where every module has a single responsibility.

| Module | Responsibility |
|---------|----------------|
| config.py | Central configuration |
| data_loader.py | Market data downloads |
| indicators.py | Technical indicators |
| market_structure.py | Support & Resistance analysis |
| scoring.py | Weighted scoring engine |
| ranking.py | Stock ranking |
| report.py | Report generation |
| scanner.py | Application orchestration |

---

# Technologies

- Python
- Pandas
- NumPy
- yfinance

---

# Development Philosophy

The objective of Swing Scanner extends beyond calculating technical indicators.

The project focuses on building a maintainable, scalable, and well-engineered trading application while learning professional software engineering practices.

Core principles include:

- Clean Architecture
- Modular Design
- Code Reusability
- Incremental Development
- Practical Software Engineering
- Continuous Improvement

---

# Current Status

**Version:** **4.0**

Status:

- ✅ Production Ready
- ✅ Successfully Tested on the Complete NIFTY 500 Universe
- ✅ Modular Architecture
- ✅ Professional Scoring Engine
- ✅ Ranking System
- ✅ Reporting System

---

# Roadmap

## Version 5.0 — Quant Research Platform

Planned features:

- Historical Backtesting Engine
- Walk-Forward Testing
- Portfolio Simulator
- Performance Analytics
- Strategy Comparison
- Weight Optimization
- Research Dashboard
- Trade Journal

See **docs/ROADMAP.md** for the complete roadmap.

---

# Learning Journey

This repository documents the evolution from learning basic Python to building a modular quantitative trading application.

The project demonstrates practical software engineering through real-world development, including architecture, refactoring, testing, debugging, documentation, and quantitative analysis.

See **docs/LEARNING_LOG.md** for the complete development history.

---

# Disclaimer

This project is intended for educational and research purposes only.

It is **not** financial advice. Always perform your own research before making investment decisions.

---

# License

This project is licensed under the MIT License.

---

# Author

**Himanshu Partani**

Computer Science Engineering Student

Python Developer • Software Engineering Enthusiast • Quantitative Trading Learner

---

# Version

**Swing Scanner v4.0.0**

*"From learning Python fundamentals to building a modular quantitative trading platform—one version at a time."*