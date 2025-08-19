# Stock Market Notification

Stock Market Notification is a Python-based application designed to fetch real-time stock data from the Brazilian stock exchange (B3) and deliver updates via WhatsApp. The project leverages the `yfinance` library to retrieve financial data and is structured for easy extension and integration with messaging platforms.

## Features

- Fetches the latest stock data for selected B3 tickers
- Modular codebase for easy maintenance and extension
- Ready for integration with WhatsApp or other messaging services
- Simple configuration for tracking multiple stocks

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Stock_Market_Notification.git
   cd Stock_Market_Notification
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Configure the tickers:**
   - Edit the `main.py` file and update the `tickers` list with the B3 stock symbols you want to track (e.g., `"PETR4.SA"`).

2. **Run the application:**
   ```bash
   python src/main.py
   ```

3. **(Optional) Integrate WhatsApp notifications:**
   - Implement your WhatsApp integration logic in `whatsapp_sender.py`.

### Example Output

```
PETR4.SA - 2025-08-14
Open: 34.50, Close: 35.10
High: 35.20, Low: 34.30, Volume: 12345678
------------------------------
```

## Project Structure

```
Stock_Market_Notification/
│   .gitignore
│   README.md
│   requirements.txt
└── src/
    │   b3_api.py
    │   main.py
    │   utils.py
    │   whatsapp_sender.py
```

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements and new features.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [yfinance](https://github.com/ranaroussi/yfinance) for financial data retrieval
- [Yahoo Finance](https://finance.yahoo.com/) for market data
