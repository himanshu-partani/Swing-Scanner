# Swing Scanner

A Python-based Swing Trading Scanner built while learning Python from scratch.

This project analyzes NSE stocks using multiple technical indicators and generates high-probability swing trading signals with built-in risk management.

---

## Features

- Live Yahoo Finance Data
- Multi Stock Scanner
- CSV Watchlist Support
- 20-Day Moving Average (MA20)
- 50-Day Moving Average (MA50)
- Previous 3-Month High Breakout
- Volume Breakout Detection
- RSI (Relative Strength Index)
- ATR (Average True Range)
- MACD (Moving Average Convergence Divergence)
- Stop Loss Calculation
- Target Calculation
- Risk Calculation
- Reward Calculation
- Reward : Risk Ratio
- Professional Console Output
- Error Handling for Invalid Tickers
- Modular Indicator Architecture

---

## Technologies

- Python
- Pandas
- yfinance
- Git
- GitHub
- VS Code

---

## Project Structure

```text
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