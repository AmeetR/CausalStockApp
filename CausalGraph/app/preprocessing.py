import yfinance as yf
import pandas as pd
from datetime import date

def get_tickers(tickers: str) -> list[yf.Ticker]:
    """
    Gets the ticker object for a given set of tickers 
    """
    return yf.Tickers(tickers)