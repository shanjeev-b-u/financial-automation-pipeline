import csv
import random
from datetime import datetime, timedelta

# Define setup variables for the 3-week simulation period
start_date = datetime(2026, 5, 10)
tickers = ["RELIANCE", "TCS", "INFY", "HDFCBANK", "ICICIBANK", "BHARTIARTL", "SBI", "ITC"]

# Prepare CSV file
filename = "simulated_trading_ledger_240.csv"
fields = ["Trade ID", "Timestamp", "Ticker", "Signal Source", "Entry Price", "Exit Price", "Quantity", "Net PnL", "Status"]

print(f"Generating {filename} with 240 simulated trade outcomes...")

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    
    for i in range(1, 241):
        trade_id = f"TRD-{1000 + i}"
        
        # Distribute timestamps evenly over a 3-week (21-day) window
        days_offset = random.randint(0, 21)
        hours_offset = random.randint(9, 15)  # Market hours
        minutes_offset = random.randint(0, 59)
        timestamp = (start_date + timedelta(days=days_offset, hours=hours_offset, minutes=minutes_offset)).strftime("%Y-%m-%d %H:%M:%S")
        
        ticker = random.choice(tickers)
        entry_price = round(random.uniform(500, 3500), 2)
        quantity = random.randint(2, 15)
        
        # Simulate the Delta: ~70% of signals passed by the LLM filter are wins
        # Traditional quant-only baseline signals without the filter hover around 40-50% wins
        is_llm_filtered = random.random() > 0.3  # 70% of our tracking features the dual-layer filter
        
        if is_llm_filtered:
            signal_source = "Quant + Gemini LLM"
            is_win = random.random() < 0.72  # High accuracy / False positives reduced
        else:
            signal_source = "Quant-Only Baseline"
            is_win = random.random() < 0.45  # Standard noisy baseline
            
        # Compute financial outcomes
        if is_win:
            change_pct = random.uniform(0.01, 0.05)  # 1% to 5% gain
            exit_price = round(entry_price * (1 + change_pct), 2)
        else:
            change_pct = random.uniform(0.01, 0.03)  # 1% to 3% standard protective stop-loss hit
            exit_price = round(entry_price * (1 - change_pct), 2)
            
        net_pnl = round((exit_price - entry_price) * quantity, 2)
        status = "Closed"
        
        writer.writerow([trade_id, timestamp, ticker, signal_source, entry_price, exit_price, quantity, net_pnl, status])

print(f"Successfully generated 240 trades! Open the file and import it directly into your Google Sheet.")