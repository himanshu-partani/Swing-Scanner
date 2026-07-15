# Swing Scanner

> **A modular Python-based Swing Trading Scanner for the Indian Stock
> Market.**

Swing Scanner is a personal software engineering project that I started
while learning Python. Instead of building small tutorial projects, I
decided to solve a real-world problem by creating a swing trading
scanner for NSE stocks.

The project has grown version by version—from basic moving averages to a complete modular stock analysis platform featuring technical indicators, market structure analysis, risk management, centralized configuration and a high-performance batch download engine.

------------------------------------------------------------------------

# Latest Release

**Current Version:** Version 3.0

Highlights

- Scanner Engine Rewrite
- Batch Download Engine
- Centralized Configuration
- Modular Architecture
- Nifty 500 Ready

------------------------------------------------------------------------

# Features

## Trend Analysis

-   20-Day Moving Average
-   50-Day Moving Average

## Momentum

-   RSI
-   MACD

## Relative Performance

-   Relative Strength vs Nifty

## Volume Analysis

-   Relative Volume
-   Volume Breakout Detection

## Breakout Analysis

-   Previous 3-Month High
-   Previous 52-Week High

## Volatility

-   ATR

## Market Structure Engine

-   Swing Point Detection
-   Zone Grouping
-   Zone Filtering
-   Nearest Support
-   Nearest Resistance
-   Zone Strength Classification
-   Distance to Support
-   Distance to Resistance

## Risk Management

-   Stop Loss
-   Target Price
-   Risk
-   Reward
-   Reward : Risk Ratio

## Scanner

-   CSV Watchlist
-   Multi-stock Scanning
-   Trading Signals
-   Professional Console Output
-   11-Point Scoring System

------------------------------------------------------------------------

# Project Structure

``` text
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
├── reports/
│
├── config.py
├── data_loader.py
├── scanner.py
├── indicators.py
├── market_structure.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

------------------------------------------------------------------------

# Architecture

    scanner.py
        │
        ├── indicators.py
        │      ├── RSI
        │      ├── ATR
        │      ├── MACD
        │      ├── Relative Strength
        │      ├── Relative Volume
        │      ├── Consolidation
        │      └── 52 Week High
        │
        └── market_structure.py
               ├── Swing Point Detection
               ├── Zone Grouping
               ├── Zone Filtering
               ├── Zone Strength
               ├── Nearest Support
               ├── Nearest Resistance
               └── Distance Calculation

------------------------------------------------------------------------

# Current Scoring (Version 3.0)

The scanner evaluates every stock using eleven independent checks.

1.  Above 20 MA
2.  Above 50 MA
3.  Previous 3-Month High Breakout
4.  Relative Volume Breakout
5.  Healthy RSI
6.  Bullish MACD
7.  Outperforming Nifty
8.  Previous 52-Week High Breakout
9.  Tight Consolidation
10. Strong Nearby Support
11. Plenty of Upside

------------------------------------------------------------------------

# Technologies

-   Python
-   Pandas
-   NumPy
-   yfinance
-   Git
-   GitHub

------------------------------------------------------------------------

# Version History

## Version 1

-   Live Data
-   Moving Averages
-   Multi-stock Scanner

## Version 1.2

-   RSI
-   ATR
-   MACD
-   Risk Management

## Version 2.0

-   CSV Watchlist
-   Better Project Structure

## Version 2.1

-   Relative Strength
-   Relative Volume

## Version 2.2

-   3-Month High
-   52-Week High
-   Better Scanner Output

## Version 2.3

-   Complete Market Structure Engine
-   Swing Point Detection
-   Support & Resistance
-   Zone Strength Classification
-   Distance to Support & Resistance
-   Market Structure Scoring
-   Extensive Testing
-   Modular Architecture Improvements

------------------------------------------------------------------------

# Upcoming Roadmap

-   Nifty 500 Scanner
-   Professional Scoring Engine
-   Ranking System
-   CSV Reports
-   Scanner Filters
-   Performance Optimization

------------------------------------------------------------------------

# Learning Outcomes

Through this project I learned:

-   Python Programming
-   Pandas
-   Financial Data Analysis
-   Technical Analysis
-   Algorithm Design
-   Modular Software Architecture
-   Refactoring
-   Git & GitHub
-   Software Documentation
-   Testing and Debugging

------------------------------------------------------------------------

# License

This project is built for educational purposes and continuous learning.
