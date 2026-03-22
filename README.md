HFT-Absorption: Modeling Microstructure Liquidity Sweeps
Project Overview
This repository contains a quantitative framework for identifying institutional absorption and liquidity sweeps within intraday tick data. The model systematizes eight years of discretionary trading experience into a rule-based engine designed to detect "retail traps"—market scenarios where aggressive liquidity is absorbed by passive institutional limit orders at key structural pivots.

Quantitative Logic
The core alpha of this strategy rests on Market Microstructure principles rather than traditional lagging indicators. It focuses on the following mechanics:

Volume-Price Divergence: Identifying clusters where high trade velocity fails to produce price displacement, signaling the presence of large passive orders (Absorption).

Order Flow Imbalance (OBI): Calculating the normalized difference between bid and ask depth to predict the direction of the subsequent "sweep."

Liquidity Reclaim: A signal is triggered when price breaches a local liquidity pool (triggering stops) and is immediately reclaimed on high relative volume, indicating institutional accumulation.

Technical Implementation
Vectorized Signal Detection: Implemented using NumPy and Pandas for high-throughput backtesting.

Performance Optimization: Core loops utilize Numba (JIT compilation) to handle high-frequency tick-by-tick data processing.

Microstructure Analysis: Features an Order Book Imbalance (OBI) calculator to measure real-time supply/demand skew.

Data & Methodology
The model is tested against historical tick-level data (L1/L2) with a focus on high-volume equity constituents.

Signal Accuracy: ~62% directional accuracy during high-volatility regimes.

Metric Focus: Information Ratio, Max Drawdown, and slippage-adjusted Sharpe Ratio.

Directory Structure
src/detector.py: Core logic for absorption and sweep detection.

src/backtest.py: Vectorized backtesting engine with transaction cost modeling.

notebooks/microstructure_analysis.ipynb: Visual proof of liquidity sweeps and OBI flips.
