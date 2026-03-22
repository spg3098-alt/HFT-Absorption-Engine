import yfinance as yf
import pandas as pd

def get_real_market_data(ticker="^NSEI"):
    """
    Fetches 1-minute interval data for NIFTY 50.
    """
    print(f"Fetching real-time data for {ticker}...")
    df = yf.download(ticker, period="2d", interval="1m")
    
    # Standardize columns for our detector
    df = df.reset_index()
    df.columns = [col.lower() for col in df.columns]
    # Handle multi-index columns if yfinance returns them
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
        
    df = df.rename(columns={'datetime': 'timestamp', 'adj close': 'adj_close'})
    return df
