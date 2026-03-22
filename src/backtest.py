import pandas as pd
import numpy as np

def run_backtest(df, initial_capital=100000, risk_per_trade=0.01):
    """
    Vectorized backtester for the Absorption Signal.
    Includes basic transaction cost modeling.
    """
    df['returns'] = df['price'].pct_change()
    
    # Strategy: Buy when signal is 1, Hold for 5 ticks (HFT style)
    df['position'] = df['signal'].shift(1).fillna(0)
    
    # Calculate Strategy Returns (accounting for 0.02% slippage/costs)
    slippage = 0.0002
    df['strategy_returns'] = df['position'] * (df['returns'] - slippage)
    
    # Performance Metrics
    cumulative_returns = (1 + df['strategy_returns']).cumprod()
    total_return = cumulative_returns.iloc[-1] - 1
    
    # Sharpe Ratio (Annualized for Intraday)
    sharpe = (df['strategy_returns'].mean() / df['strategy_returns'].std()) * np.sqrt(252 * 6.5 * 60)
    
    # Max Drawdown
    rolling_max = cumulative_returns.cummax()
    drawdown = (cumulative_returns - rolling_max) / rolling_max
    max_dd = drawdown.min()

    print(f"--- Backtest Results ---")
    print(f"Total Return: {total_return:.2%}")
    print(f"Sharpe Ratio: {sharpe:.2f}")
    print(f"Max Drawdown: {max_dd:.2%}")
    
    return df
