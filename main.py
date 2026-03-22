import pandas as pd
from src.data_loader import get_real_market_data
from src.detector import process_tick_data
from src.backtest import run_backtest

def main():
    # 1. Fetch data (Set to NIFTY 50 by default)
    # Note: For the hackathon tomorrow, you can swap this for pd.read_csv()
    try:
        raw_data = get_real_market_data("^NSEI")
        
        if raw_data.empty:
            print("Error: No data fetched. Check your internet connection.")
            return

        # 2. Run the HFT Absorption Logic
        print("Analyzing Institutional Traps...")
        processed_data = process_tick_data(raw_data)
        
        # 3. Identify and display signals
        signals = processed_data[processed_data['signal'] == 1]
        print(f"Analysis Complete. Found {len(signals)} potential Institutional Traps.")
        
        # 4. Run Backtest if signals exist
        if not signals.empty:
            print(signals[['timestamp', 'price', 'volume']].tail())
            run_backtest(processed_data)
        else:
            print("No actionable signals found in the current dataset.")

    except Exception as e:
        print(f"An error occurred during execution: {e}")

if __name__ == "__main__":
    main()
