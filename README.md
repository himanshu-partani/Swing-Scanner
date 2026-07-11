# 📈 Swing Scanner

A Python-based Swing Trading Scanner built while learning Python from scratch.

Instead of learning Python through isolated exercises, this project applies programming concepts to a real-world trading application. The scanner downloads live NSE stock data, calculates multiple technical indicators, evaluates swing trading conditions, and generates trading signals using a modular architecture.

---

## ✨ Features

### Core

* Live NSE stock data using Yahoo Finance
* CSV-based watchlist
* Modular architecture
* Professional console output
* Error handling

### Technical Indicators

* 20-Day Moving Average (MA20)
* 50-Day Moving Average (MA50)
* RSI (Relative Strength Index)
* ATR (Average True Range)
* MACD
* MACD Signal Line
* MACD Histogram
* Relative Strength vs Nifty

### Breakout Detection

* Previous 3-Month High
* Previous 52-Week High
* Relative Volume (RVOL)

### Trade Planning

* Stop Loss
* Target Price
* Risk Calculation
* Reward Calculation
* Reward : Risk Ratio

### Scanner

* 8-Point Swing Scoring System
* Trading Signals
* Professional formatted output

---

## 📁 Project Structure

```
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

## 🛠️ Technologies Used

* Python
* Pandas
* yfinance
* Git
* GitHub

---

## 📊 Current Scanner Logic

The scanner evaluates each stock using the following conditions:

* Above 20-Day Moving Average
* Above 50-Day Moving Average
* 3-Month High Breakout
* Relative Volume Breakout
* Healthy RSI (50–70)
* Bullish MACD
* Outperforming Nifty
* 52-Week High Breakout

Each satisfied condition earns one point.

Maximum Score: **8/8**

---

## 🚀 Current Version

**Version 2.2**

### Highlights

* Added Previous 52-Week High Detection
* Added Relative Volume (RVOL)
* Upgraded from a 7-point scanner to an 8-point scoring system
* Improved breakout calculations using fixed trading-day lookback windows
* Improved console formatting and naming consistency

---

## 🎯 Future Roadmap

* Consolidation Detection
* Support & Resistance
* Automatic CSV Reports
* Ranked Scanner Results
* Portfolio Scanner
* Streamlit Dashboard
* Charts
* Telegram Alerts
* AI-Based Trade Explanations

---

## 📚 Learning Goals

This project is part of my journey of learning:

* Python
* Pandas
* Financial Data Analysis
* Technical Indicators
* Software Architecture
* Git & GitHub
* Clean Code Practices

---

## 🤝 Contributions

This project is currently a personal learning project. Suggestions and improvements are always welcome.

---

## ⭐ Acknowledgements

Market data is provided through Yahoo Finance using the `yfinance` Python library.
