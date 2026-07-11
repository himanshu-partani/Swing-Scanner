# 📘 LEARNING_LOG

## Project: Swing Scanner

This document tracks what I learned while building the Swing Scanner project.

---

# Version 1.0

### Python Concepts

* Variables
* Loops
* Functions
* Lists
* Reading CSV files
* Error handling using `try` and `except`

### Libraries

* Pandas basics
* yfinance
* Working with DataFrames

### Features Built

* Live stock data download
* 20-Day Moving Average
* 50-Day Moving Average
* Multi-stock scanner

---

# Version 1.1

### Learned

* Better project organization
* Cleaner console output
* Modular thinking
* Code readability improvements

---

# Version 1.2

### Technical Indicators

* RSI
* ATR

### Trade Planning

* Stop Loss
* Target Price
* Risk
* Reward
* Reward : Risk Ratio

### Software Engineering

* Created `indicators.py`
* Moved calculations into reusable functions
* Improved project structure

---

# Version 2.0

### Data Management

* Switched from a hardcoded watchlist to a CSV-based watchlist
* Improved error handling
* Better scanner architecture

### Git & GitHub

* Learned Git basics
* Created a GitHub repository
* Managed commits and version history

---

# Version 2.1

### Technical Indicators

* MACD
* Signal Line
* Histogram
* Relative Strength vs Nifty

### Scanner Improvements

* 7-Point Swing Scoring System
* Professional scanner output
* Better modular design
* Cleaner code organization

---

# Version 2.2

## New Features

### Previous 52-Week High

Learned:

* Difference between calendar days and trading days
* Why a trading year is approximately 252 trading sessions
* Why today's candle should be excluded while calculating previous highs
* Fixed lookback windows instead of relying on the download period
* Difference between 3-Month High and 52-Week High breakouts

---

### Relative Volume (RVOL)

Learned:

* Relative Volume formula

  RVOL = Today's Volume / 20-Day Average Volume

* Why traders prefer Relative Volume over comparing raw volume numbers

* How Relative Volume measures trading activity relative to normal participation

* Using RVOL as a cleaner breakout confirmation signal

---

### Software Engineering

Learned:

* Better function design
* Choosing between variables and reusable functions
* Cleaner naming conventions
* Using constants instead of magic numbers
* Consistent console formatting
* Improving code readability
* Thinking about edge cases (such as newly listed stocks)

---

### Architecture Improvements

* Improved scanner modularity
* Fixed 3-Month High calculation using a fixed 63-day lookback
* Added Previous 52-Week High calculation
* Upgraded from a 7-point scanner to an 8-point scoring system

---

# Overall Progress

Through this project, I have learned:

* Python fundamentals
* Pandas
* Working with financial market data
* Technical analysis indicators
* Modular software design
* Git & GitHub
* Writing cleaner and more maintainable code
* Building a real-world Python project step by step instead of following tutorials

---

## Next Version

**Version 2.3**

* Consolidation Detection
* Further improvements to the Swing Scanner
