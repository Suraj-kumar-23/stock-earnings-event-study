# Fetch the stock and earning data by  API
import requests
import pandas as pd

API_KEY = "APqYsf6eDQNzY5XkadK0My2F4EWgg7LS"

def get_stock_data(symbol="AAPL"):
    
    url = f"https://financialmodelingprep.com/stable/historical-price-eod/full?symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    df = pd.DataFrame(data)
    
    df["date"] = pd.to_datetime(df["date"])
    
    return df


def get_earnings_data(symbol="AAPL"):
    
    url = f"https://financialmodelingprep.com/stable/earnings-calendar?symbol={symbol}&apikey={API_KEY}"
    
    response = requests.get(url)
    data = response.json()
    
    df = pd.DataFrame(data)
    
    df["date"] = pd.to_datetime(df["date"])
    
    return df
