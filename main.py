import ccxt
import pandas as pd
import asyncio
import requests
import config
from datetime import datetime, timezone
from telegram import Update
from telegram.ext import Application, CommandHandler

interval = '1m'

# Initialize bybit client
bybit = ccxt.bybit({
    'apiKey': config.API_KEY,
    'secret': config.API_SECRET,
})

# Dictionary to store the last alert messages for each symbol
last_alert_messages = {}

# List of selected symbols from Telegram (global variable)
selected_symbols = []

# Function to get historical candlestick data
def get_historical_data(symbol, interval, limit=20):
    ohlcv = bybit.fetch_ohlcv(symbol, interval, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df

# Function to get day open price
def get_day_open_price(symbol):
    day_ohlcv = bybit.fetch_ohlcv(symbol, '1d', limit=3)
    df_day = pd.DataFrame(day_ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df_day['timestamp'] = pd.to_datetime(df_day['timestamp'], unit='ms')
    df_day.set_index('timestamp', inplace=True)
    day_open_price = df_day['close'].iloc[-2]
    return day_open_price

# Function to calculate SMA
def calculate_sma(df, period):
    return df['close'].rolling(window=period).mean()

# Function to check SMA crossover against day open price
def check_sma_crossover_vs_day_open(df, day_open_price, short_period=3):
    df['sma_short'] = calculate_sma(df, short_period)  # Already returns a Series, so no squeeze needed
    cross_over = df['sma_short'].iloc[-2] > day_open_price
    cross_under = df['sma_short'].iloc[-2] < day_open_price
    return cross_over, cross_under

# Function to get previous day's amplitude ratio
def get_previous_day_amplitude(symbol):
    daily_ohlcv = bybit.fetch_ohlcv(symbol, '1d', limit=5)
    df_daily = pd.DataFrame(daily_ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df_daily['timestamp'] = pd.to_datetime(df_daily['timestamp'], unit='ms')
    df_daily.set_index('timestamp', inplace=True)
    
    prev_day_high = df_daily['high'].iloc[-2]
    prev_day_low = df_daily['low'].iloc[-2]
    
    amplitude_ratio = prev_day_high / prev_day_low
    return amplitude_ratio

# Function to send a message to 3commas using a webhook
def send_3commas_message(symbol, action, close_price, bot_uuid, secret):
    if last_alert_messages.get(symbol) != action:
        timestamp = datetime.now(timezone.utc).isoformat()
        payload = {
            "secret": secret,
            "max_lag": "300",
            "timestamp": timestamp,
            "trigger_price": str(close_price),
            "tv_exchange": "bybit",
            "tv_instrument": symbol.replace('/', '') + '.P',
            "action": action,
            "bot_uuid": bot_uuid
        }

        try:
            url = config.THREE_COMMAS_WEBHOOK_URL
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                print(f"Successfully sent alert for {symbol} with action {action} to bot {bot_uuid}")
                last_alert_messages[symbol] = action
            else:
                print(f"Failed to send alert for {symbol} to bot {bot_uuid}: {response.content}")

        except requests.RequestException as e:
            print(f"Error sending request for {symbol} to bot {bot_uuid}: {e}")

# Updated function to set symbols by matching against config.AVAILABLE_SYMBOLS
async def set_symbols(update: Update, context) -> None:
    global selected_symbols
    user_symbols = context.args

    if user_symbols:
        # Convert user input to uppercase and filter only those in config.AVAILABLE_SYMBOLS
        valid_symbols = [symbol.upper() for symbol in user_symbols if symbol.upper() in config.AVAILABLE_SYMBOLS]
        invalid_symbols = [symbol.upper() for symbol in user_symbols if symbol.upper() not in config.AVAILABLE_SYMBOLS]

        # Add valid symbols to the selected_symbols list, avoiding duplicates
        new_symbols = [symbol for symbol in valid_symbols if symbol not in selected_symbols]
        selected_symbols.extend(new_symbols)

        # Prepare a response message
        response_message = ""
        if new_symbols:
            response_message += f"Symbols updated: {', '.join(selected_symbols)}\n"
        if invalid_symbols:
            response_message += f"Invalid symbols (not available): {', '.join(invalid_symbols)}"
        if not new_symbols and not invalid_symbols:
            response_message = "All provided symbols are already in the list."

        # Send the response message to the user
        await update.message.reply_text(response_message)
    else:
        await update.message.reply_text("No symbols provided. Usage: /set_symbols BTC/USDT ETH/USDT")

# Command to reset symbols
async def reset_symbols(update: Update, context) -> None:
    global selected_symbols
    selected_symbols = []
    await update.message.reply_text("Symbols have been reset.")

# Main trading function
async def main_trading():
    while True:
        for symbol in selected_symbols:
            try:
                historical_data = get_historical_data(symbol, interval)
                day_open_price = get_day_open_price(symbol)
                cross_over, cross_under = check_sma_crossover_vs_day_open(historical_data, day_open_price)
                close_price = historical_data['close'].iloc[-1]
                amplitude_ratio = get_previous_day_amplitude(symbol)
                
                print(f"Amplitude ratio for {symbol}: {amplitude_ratio}")
                
                if amplitude_ratio >= 1.01:
                    if cross_over:
                        send_3commas_message(symbol, "enter_long", close_price, "00830f96-c475-4c3e-9e38-9a4495e3b78c", config.SECRET_1)
                        #send_3commas_message(symbol, "enter_long", close_price, "00830f96-c475-4c3e-9e38-9a4495e3b78c", config.SECRET_2)
                    elif cross_under:
                        send_3commas_message(symbol, "enter_short", close_price, "00830f96-c475-4c3e-9e38-9a4495e3b78c", config.SECRET_1)
                        #send_3commas_message(symbol, "enter_short", close_price, "00830f96-c475-4c3e-9e38-9a4495e3b78c", config.SECRET_2)
                else:
                    print(f"Amplitude condition not met for {symbol}, skipping...")

            except Exception as e:
                print(f"Error processing {symbol}: {e}")

        await asyncio.sleep(10)

# Start Telegram bot
async def start_telegram_bot():
    application = Application.builder().token(config.TELEGRAM_TOKEN).build()
    
    # Initialize the application (fixes the error)
    await application.initialize()

    application.add_handler(CommandHandler('set_symbols', set_symbols))
    application.add_handler(CommandHandler('reset_symbols', reset_symbols))

    await application.start()
    await application.updater.start_polling()

# Main function to run both bot and trading
async def main():
    await asyncio.gather(
        start_telegram_bot(),
        main_trading()
    )

# Run the main function
if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()

    asyncio.run(main())