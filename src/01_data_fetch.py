# src/01_data_fetch.py
import yfinance as yf
import pandas as pd
import os
import logging
from datetime import datetime, timedelta
from time import sleep
from typing import List

logging.basicConfig(level=logging.INFO, filename="data_fetch.log",
                    format="%(asctime)s %(levelname)s %(message)s")

DATA_DIR = "price-predictor/data/raw"
os.makedirs(DATA_DIR, exist_ok=True)

def date_range_str(years=5):
    end = datetime.utcnow().date()
    start = end - timedelta(days=years*365)
    return start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")

def download_ticker(ticker: str, start: str, end: str, interval: str="1d", retries=3):
    fname = os.path.join(DATA_DIR, f"{ticker.replace('/','_')}.csv")
    if os.path.exists(fname):
        logging.info(f"Found cached file {fname}")
        return pd.read_csv(fname, parse_dates=["Date"])
    attempt = 0
    while attempt < retries:
        try:
            logging.info(f"Downloading {ticker} ({start}..{end}), attempt {attempt+1}")
            df = yf.download(ticker, start=start, end=end, interval=interval, progress=False)
            if df.empty:
                logging.warning(f"No data for {ticker}")
                return pd.DataFrame()
            df = df.reset_index()
            df.to_csv(fname, index=False)
            logging.info(f"Saved {fname} ({len(df)} rows)")
            return df
        except Exception as e:
            logging.error(f"Error downloading {ticker}: {e}")
            attempt += 1
            sleep(2 ** attempt)
    logging.error(f"Failed to download {ticker} after {retries} attempts")
    return pd.DataFrame()

def download_many(tickers: List[str], years: int = 5):
    start, end = date_range_str(years)
    results = {}
    for t in tickers:
        df = download_ticker(t, start, end)
        results[t] = df
    return results

if __name__ == "__main__":
    TICKS = [
                            "GC=F", "SI=F", "CL=F", "PL=F", "PA=F",  # Commodities
                            "BTC-USD", "ETH-USD", "XRP-USD", "LTC-USD", "ADA-USD",  # Cryptocurrencies
                            "AAPL", "MSFT", "DELL", "HPQ", "NVDA", "INTC", "GOOGL", "QCOM", "SNE", "XIACF",  # Mobile and tech
                            "LNVGY", "ASUSF", "AMD",  # Laptops and components
                            "TSLA", "F", "GM", "NIO", "TM",  # Cars
                            "SSNLF", "GRMN", "LOGI", "SONO"  # Electronics
                        ]  # edit this list with real tickers
    download_many(TICKS, years=5)
