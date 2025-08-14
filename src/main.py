from b3_api import get_stock_data

def main():
    tickers = ["PETR4.SA", "VALE3.SA", "ITUB4.SA"]
    for ticker in tickers:
        data = get_stock_data(ticker)
        if data:
            print(f"{data['ticker']} - {data['date']}")
            print(f"Open: {data['open']}, Close: {data['close']}")
            print(f"High: {data['high']}, Low: {data['low']}, Volume: {data['volume']}")
            print("-" * 30)
        else:
            print(f"No data found for {ticker}")

if __name__ == "__main__":
    main()