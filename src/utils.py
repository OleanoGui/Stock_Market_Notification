def format_stock_data(data: dict) -> str:
    if not data:
        return "No data available."
    return (
        f"{data['ticker']} - {data['date']}\n"
        f"Open: {data['open']}, Close: {data['close']}\n"
        f"High: {data['high']}, Low: {data['low']}, Volume: {data['volume']}\n"
        + "-" * 30
    )