# 🚀 Swing Scanner

> **A Professional Python-Based Swing Trading Scanner for the Indian Stock Market**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Latest-green.svg)
![Yahoo Finance](https://img.shields.io/badge/Data-Yahoo%20Finance-orange.svg)
![Version](https://img.shields.io/badge/Version-3.2-success.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

---

# Overview

Swing Scanner is a modular Python application designed to identify high-quality swing trading opportunities in the Indian stock market using technical analysis, market structure, and a professional weighted scoring engine.

The project started as a Python learning journey and has evolved into a structured software engineering project featuring clean architecture, reusable modules, centralized configuration, batch data processing, and an extensible scoring system.

Version **3.2** represents the first major architectural milestone of the project.

---

# Features

## Market Data

* Live market data from Yahoo Finance
* Batch download engine
* Watchlist scanning
* Nifty 500 scanning
* Automatic Nifty benchmark download

---

## Technical Indicators

* Moving Average 20
* Moving Average 50
* RSI
* ATR
* MACD
* Relative Strength vs Nifty
* Relative Volume
* Previous 3-Month High
* 52-Week High
* Consolidation Detection

---

## Market Structure Engine

* Swing Point Detection
* Support Zones
* Resistance Zones
* Zone Grouping
* Zone Filtering
* Zone Strength Classification
* Nearest Support Detection
* Nearest Resistance Detection
* Distance Calculations

---

## Trade Analysis

* Risk
* Reward
* Risk : Reward Ratio
* Upside Potential

---

## Professional Scoring Engine

Weighted **100 Point** scoring system.

Categories:

* Trend
* Momentum
* Volume
* Market Structure
* Trade Quality

Professional ratings:

| Score    | Rating                  |
| -------- | ----------------------- |
| 90–100   | ⭐⭐⭐⭐⭐ Elite Swing Trade |
| 75–89    | ⭐⭐⭐⭐☆ Strong Setup      |
| 60–74    | ⭐⭐⭐☆☆ Watchlist         |
| 40–59    | ⭐⭐☆☆☆ Average           |
| Below 40 | ⭐☆☆☆☆ Avoid             |

---

# Version 3.2 Highlights

## Modular Architecture

The scanner has been reorganized into specialized modules with clear responsibilities.

## Centralized Configuration

All configurable values are maintained inside a single configuration file.

## Batch Download Engine

Downloads market data for multiple stocks simultaneously for significantly improved performance.

## Report Object Architecture

Analysis is converted into structured report objects before presentation.

## Decision Engine

The scoring engine converts raw technical data into actionable trading decisions.

## Ranking Engine

All scanned stocks are ranked from highest to lowest score.

## Multiple Scan Modes

```python
SCAN_MODE = "watchlist"
```

Scans stocks listed in:

```
data/stocks.csv
```

or

```python
SCAN_MODE = "nifty500"
```

Scans the complete Nifty 500 universe.

---

## Multiple Output Modes

### Full Mode

```python
OUTPUT_MODE = "full"
```

Displays detailed analysis for every scanned stock.

### Summary Mode

```python
OUTPUT_MODE = "summary"
```

Displays:

* Top Swing Opportunities
* Market Summary

Designed for large scans such as Nifty 500.

---

# Project Structure

```text
Swing Scanner
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
                    scanner.py
                         │
     ┌──────────────┬──────────────┬──────────────┐
     ▼              ▼              ▼
indicators.py  market_structure.py scoring.py
                         │
                         ▼
                    report.py
                         │
                         ▼
                    ranking.py
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

All settings are centralized inside:

```
config.py
```

Examples:

```python
SCAN_MODE = "watchlist"
OUTPUT_MODE = "summary"
```

Additional configuration includes:

* Indicator periods
* Scoring weights
* Download period
* Consolidation thresholds
* Zone grouping thresholds

---

# Scan Modes

## Watchlist Mode

Scans stocks listed inside:

```
data/stocks.csv
```

Best for personal watchlists.

---

## Nifty 500 Mode

Scans the entire Nifty 500 universe.

Before the first scan, prepare the ticker list using:

```bash
python tools/prepare_nifty500.py
```

---

# Output

## Full Report

Displays detailed analysis including:

* Technical indicators
* Category scores
* Trade metrics
* Positive signals
* Weaknesses
* Overall rating

---

## Summary Report

Displays:

* Top ranked opportunities
* Market statistics
* Rating distribution

Ideal for scanning hundreds of stocks.

---

# Software Design

Swing Scanner follows a modular architecture where every module has a single responsibility.

| Module              | Responsibility                     |
| ------------------- | ---------------------------------- |
| config.py           | Central configuration              |
| data_loader.py      | Data loading and downloads         |
| indicators.py       | Technical indicators               |
| market_structure.py | Support & resistance analysis      |
| scoring.py          | Decision engine                    |
| ranking.py          | Ranking scanned stocks             |
| report.py           | Report generation and presentation |
| scanner.py          | Application orchestration          |

---

# Technologies

* Python
* Pandas
* NumPy
* yfinance

---

# Development Philosophy

The goal of this project is not simply to calculate indicators.

The focus is on building a maintainable, scalable, and well-engineered trading application while learning professional Python software development practices.

Every version prioritizes:

* Clean architecture
* Readable code
* Modular design
* Reusability
* Incremental improvement
* Practical software engineering

---

# Current Status

**Version:** 3.2

Status:

✅ Stable

✅ Feature Complete

✅ Modular Architecture

✅ Release Ready

---

# Roadmap

Planned future improvements include:

* CSV report export
* Portfolio scanner
* Interactive charts
* Streamlit dashboard
* Telegram notifications
* AI-assisted trade explanations
* Backtesting engine
* Strategy optimization
* Broker API integration

See **docs/ROADMAP.md** for the complete roadmap.

---

# Learning Journey

This repository documents the evolution from learning basic Python to building a modular financial analysis application.

The project emphasizes learning through real-world software development, including architecture, refactoring, testing, and documentation.

See **docs/LEARNING_LOG.md** for the complete development history.

---

# License

This project is licensed under the MIT License.

---

# Author

**Himanshu Partani**

Computer Science Engineering Student

Python Developer | Software Engineering Enthusiast | Swing Trading Learner

---

# Version

**Swing Scanner v3.2**

*"From learning Python to building professional software—one version at a time."*
