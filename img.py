import ccxt
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
from io import BytesIO
import asyncio
import nest_asyncio
from telegram import Bot
import config4  # Import the config module

interval = '4h'  # 4-hour candlesticks

# Initialize Bybit client
bybit = ccxt.bybit({
    'apiKey': config4.API_KEY,
    'secret': config4.API_SECRET,
})

# Dictionary to store the last alert messages for each symbol
last_alert_messages = {}

# Function to get historical candlestick data
def get_historical_data(symbol, interval, limit=50):
    ohlcv = bybit.fetch_ohlcv(symbol, interval, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    
    # Renaming columns to match the expected format
    df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    return df

# Updated function to plot candlesticks and return an image buffer
def plot_candles(df, symbol, title):
    # Ensure the index is in datetime format and the data is in the correct format for mplfinance
    mpf_data = df[['Open', 'High', 'Low', 'Close']].copy()

    # Create custom market colors for up and down candlesticks
    mc = mpf.make_marketcolors(up='#2fc71e', down='#ed2f1a', inherit=True)

    # Create a custom style using the market colors and other style settings
    s = mpf.make_mpf_style(base_mpl_style=['bmh', 'dark_background'], marketcolors=mc, y_on_right=True)

    # Prepare the plot figure with a custom ratio and return figure for further customization
    fig, axlist = mpf.plot(mpf_data,
                           figratio=(10, 6),
                           type="candle",
                           style=s,
                           tight_layout=True,
                           datetime_format='%H:%M',
                           ylabel="Precio ($)",
                           returnfig=True)

    # Add Title with a more commonly available font
    axlist[0].set_title(f"{symbol} - {title}", fontsize=25, style='italic', fontfamily='sans-serif')  # Changed fontfamily

    # Adjust layout and save plot to a BytesIO object (removed plt.tight_layout)
    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')  # Added bbox_inches='tight'
    buf.seek(0)

    # Close the figure to avoid memory overflow
    plt.close(fig)

    return buf

# Function to send Telegram message and image (now defined as async)
async def send_telegram_message(symbol, message, image_buffer):
    # Check if the current message is the same as the previous one for this symbol
    if last_alert_messages.get(symbol) != message:
        try:
            await telegram_bot.send_message(chat_id=config4.CHAT_ID, text=message)
            # Send image
            await telegram_bot.send_photo(chat_id=config4.CHAT_ID, photo=image_buffer)
            # Update the last alert message for this symbol
            last_alert_messages[symbol] = message
        except Exception as e:
            print(f"Error sending message for {symbol}: {e}")

# Main function (now defined as async)
async def main():
    while True:
        for symbol in config4.SELECTED_SYMBOLS:
            try:
                historical_data = get_historical_data(symbol, interval)
                
                # Check amplitude ratio for the latest candle
                latest_candle = historical_data.iloc[-1]
                amplitude_ratio = latest_candle['High'] / latest_candle['Low']
                
                if amplitude_ratio > 1.1:
                    message = f'Amplitude ratio > 1.1 detected on #{symbol}'
                    title = f'Amplitude Alert for {symbol}'
                    # Plot and get image buffer
                    image_buffer = plot_candles(historical_data, symbol, title)
                    await send_telegram_message(symbol, message, image_buffer)

            except Exception as e:
                print(f"Error processing {symbol}: {e}")

        # Sleep for a specified interval before checking again
        await asyncio.sleep(300)  # Adjust the sleep duration as needed

# Initialize Telegram Bot
telegram_bot = Bot(token=config4.TELEGRAM_TOKEN)

# Use nest_asyncio to allow running asyncio in Jupyter notebooks
nest_asyncio.apply()

# Create and run the event loop
asyncio.run(main())