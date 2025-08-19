from src.b3_api import get_stock_data
from src.whatsapp_sender import send_whatsapp_message
from src.utils import format_stock_data
from dotenv import load_dotenv
import os

load_dotenv()

def load_tickers(filepath: str):
    with open(filepath, "r") as f:
        return [line.strip() for line in f if line.strip()]

def main():
    tickers = load_tickers("my_stocks.txt")
    messages = ["Test about WhatsApp integration:"]
    for ticker in tickers:
        data = get_stock_data(ticker)
        messages.append(format_stock_data(data))
    final_message = "\n\n".join(messages)
    phone_number = os.getenv("DEST_PHONE_NUMBER")
    send_whatsapp_message(phone_number, final_message)

if __name__ == "__main__":
    main()