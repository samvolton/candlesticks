import pandas
import yfinance as yf
def is_consolidating(df, percentage=2):
    recent_candlesticks = df[-15:]
    
    max_close = recent_candlesticks['Close'].max()
    min_close = recent_candlesticks['Close'].min()

    threshold = 1 - (percentage / 100)
    if min_close > (max_close * threshold):
        return True        

    return False

def is_breaking_out(df, percentage=2.5):
    last_close = df[-1:]['Close'].values[0]

    if is_consolidating(df[:-1], percentage=percentage):
        recent_closes = df[-16:-1]

        if last_close > recent_closes['Close'].max():
            return True

    return False

def analyze_stocks(tickers):
    for ticker in tickers:
        data = yf.download(ticker, start="2023-01-01", end="2020-04-01")
        
        if is_consolidating(data, percentage=2.5):
            print("{} is consolidating".format(ticker))

        if is_breaking_out(data):
            print("{} is breaking out".format(ticker))
