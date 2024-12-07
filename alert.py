import ccxt
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import asyncio
import nest_asyncio
from telegram import Bot
import config3  # Import the config3 module

interval = '4h'  # 1-day candlesticks

# Initialize bybitclient
bybit= ccxt.bybit({
    'apiKey': config3.API_KEY,
    'secret': config3.API_SECRET,
})

# Dictionary to store the last alert messages for each symbol
last_alert_messages = {}

# Function to get historical candlestick data
def get_historical_data(symbol, interval, limit=10):
    ohlcv = bybit.fetch_ohlcv(symbol, interval, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df

# Function to calculate amplitude ratio
def calculate_amplitude_ratio(df):
    prev_day_high = df['high'].iloc[-1]
    prev_day_low = df['low'].iloc[-1]
    amplitude_ratio = prev_day_high / prev_day_low
    return amplitude_ratio

# Function to send Telegram message (async)
async def send_telegram_message(symbol, message):
    # Check if the current message is the same as the previous one for this symbol
    if last_alert_messages.get(symbol) != message:
        await telegram_bot.send_message(chat_id=config3.CHAT_ID, text=message)
        # Update the last alert message for this symbol
        last_alert_messages[symbol] = message

# Main function (async)
async def main():
    while True:
        for symbol in config3.SELECTED_SYMBOLS:
            try:
                # Get historical data
                historical_data = get_historical_data(symbol, interval)
                
                # Calculate amplitude ratio
                amplitude_ratio = calculate_amplitude_ratio(historical_data)

                # If amplitude ratio is significant, send an alert
                if amplitude_ratio >= 1.10:  # Change threshold as needed
                    message = f'/set_symbols #{symbol} - {amplitude_ratio:.2f}'
                    await send_telegram_message(symbol, message)

            except Exception as e:
                print(f"Error processing {symbol}: {e}")

        # Sleep for a specified interval before checking again
        await asyncio.sleep(900)  # Adjust the sleep duration as needed

# Initialize Telegram Bot
telegram_bot = Bot(token=config3.TELEGRAM_TOKEN)

# Use nest_asyncio to allow running asyncio in Jupyter notebooks
nest_asyncio.apply()

# Create and run the event loop
asyncio.run(main())
