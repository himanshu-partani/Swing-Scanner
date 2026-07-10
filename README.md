# Swing Scanner

A Python-based stock swing trading scanner built while learning Python from scratch.

This project started as a way to learn Python but has gradually evolved into a modular technical analysis tool capable of scanning multiple Indian stocks using live Yahoo Finance data.

---

## Features

### Market Data
- Live stock data from Yahoo Finance
- CSV watchlist support
- Error handling for invalid stocks
- Modular project architecture

### Technical Indicators
- 20-Day Moving Average (MA20)
- 50-Day Moving Average (MA50)
- RSI (Relative Strength Index)
- ATR (Average True Range)
- MACD
- Signal Line
- MACD Histogram
- Relative Strength vs Nifty

### Breakout Detection
- Previous 3-Month High Breakout
- Volume Breakout Detection

### Trade Planning
- ATR Based Stop Loss
- ATR Based Target
- Risk Calculation
- Reward Calculation
- Reward : Risk Ratio

### Scoring System
- 7-Point Swing Scoring System

Current scoring factors:

- Above MA20
- Above MA50
- Previous High Breakout
- Volume Breakout
- Healthy RSI
- Bullish MACD
- Outperforming Nifty

---

## Technologies Used

- Python
- Pandas
- yfinance
- Git
- GitHub

---

## Project Structure

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

## Current Version

Version 2.1

Latest addition:

- Relative Strength vs Nifty
- Nifty downloaded once for better performance
- 7-Point Scoring System
- Improved professional console output

---

## Future Plans

- 52 Week High Detection
- Relative Volume
- Consolidation Detection
- Professional Reports
- Ranking Engine
- Nifty 500 Scanner
- Streamlit Dashboard
- AI Swing Scanner