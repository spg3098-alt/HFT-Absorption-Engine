import pandas as pd
import numpy as np
from src.detector import process_tick_data

# Create fake 'Trap' data
data = {
    'timestamp': pd.date_range(start='2026-03-22', periods=100, freq='S'),
    # Price drops, stays flat during absorption, then shoots up
    'price': [100.0]*40 + [99.5]*10 + [99.5]*5 + [101.0]*45, 
    # Volume spikes exactly during the flat price period
    'volume': [100]*50 + [5000]*5 + [100]*45 
}

df_test = pd.DataFrame(data)

# Run your detector
results = process_tick_data(df_test)

# Check if signal triggered
signals_found = results[results['signal'] == 1]

if not signals_found.empty:
    print("✅ SUCCESS: The engine detected the Institutional Trap.")
    print(signals_found[['timestamp', 'price', 'volume']])
else:
    print("❌ FAILED: Signal not triggered. Check threshold logic.")
