import pandas as pd
import yfinance as yf
import config

def load_watchlist():
    watchlist = pd.read_csv(config.WATCHLIST_FILE)
    return watchlist["Ticker"].tolist()

def download_nifty_data():
    nifty_data = yf.download(
        config.MARKET_INDEX,
        period=config.DOWNLOAD_PERIOD,
        progress=False
    )
    nifty_data.columns = nifty_data.columns.get_level_values(0)
    nifty_data = nifty_data.dropna(subset=["Close"])
    return nifty_data

def download_market_data(tickers):
    market_data = {}
    all_data = yf.download(
    tickers=tickers,
    period=config.DOWNLOAD_PERIOD,
    progress=False,
    group_by="ticker")
    for ticker in tickers:
        data = all_data[ticker]
        data = data.dropna(subset=["Close"])
        market_data[ticker] = data
    return market_data

def load_nifty500():
    df = pd.read_csv("data/nifty500.csv")
    return df["Ticker"].tolist()