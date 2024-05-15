import yfinance as yf
import time
from datetime import datetime

# Function to get the latest premarket price
def get_premarket_price(ticker):
    data = ticker.history(period="1d", interval="1m", prepost=True)
    premarket_data = data.between_time('04:00', '09:30')
    if not premarket_data.empty:
        return premarket_data['Close'].iloc[-1]
    else:
        return None

# Ticker symbol
ticker = yf.Ticker("GME")

# Continuously fetch premarket price every 5 seconds
try:
    while True:
        # Check if the current time is within the premarket trading hours (adjusted for time in UK)
        current_time = datetime.now().time()
        if current_time >= datetime.strptime('09:00', '%H:%M').time() and current_time <= datetime.strptime('14:30', '%H:%M').time():
            premarket_price = get_premarket_price(ticker)
            if premarket_price is not None:
                print(f"Current GME Premarket Price: {premarket_price} at {datetime.now()}")
            else:
                print("No premarket data available at the moment")
        else:
            print("Outside of premarket trading hours")
        
        # Sleep for 5 seconds
        time.sleep(60)

except KeyboardInterrupt:
    print("Stopped fetching premarket prices")