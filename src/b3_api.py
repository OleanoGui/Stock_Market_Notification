import yfinance as yf

def get_stock_data(ticker: str):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    if data.empty:
        return None
    last_quote = data.iloc[-1]
    return {
        "ticker": ticker,
        "date": last_quote.name.strftime("%Y-%m-%d"),
        "open": last_quote["Open"],
        "close": last_quote["Close"],
        "high": last_quote["High"],
        "low": last_quote["Low"],
        "volume": int(last_quote["Volume"])
    }