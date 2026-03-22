import pandas as pd
import numpy as np
from numba import njit

@njit
def find_absorption_zones(prices, volumes, window=50, threshold=3.0):
    """
    Numba-optimized loop to find Price Absorption.
    Absorption = High Volume + Low Price Movement.
    """
    n = len(prices)
    signals = np.zeros(n)
    
    for i in range(window, n):
        # Calculate rolling average volume
        avg_vol = np.mean(volumes[i-window:i])
        
        # Check for Volume Spike
        if volumes[i] > (avg_vol * threshold):
            # Check if price stalled (Price Change < 0.01%)
            price_change = abs(prices[i] - prices[i-1]) / prices[i-1]
            if price_change < 0.0001:
                signals[i] = 1  # Potential Institutional Trap/Absorption
                
    return signals

def process_tick_data(df):
    """
    Wrapper to handle DataFrame and call optimized logic.
    """
    # Ensure data is sorted by time
    df = df.sort_values('timestamp')
    
    # Extract arrays for Numba
    prices = df['price'].values
    volumes = df['volume'].values
    
    # Run Detector
    df['is_absorption'] = find_absorption_zones(prices, volumes)
    
    # Identify the 'Sweep' (Price breaks out after absorption)
    df['signal'] = (df['is_absorption'].shift(1) == 1) & (df['price'].diff() > 0)
    
    return df
