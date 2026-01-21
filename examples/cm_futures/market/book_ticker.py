#!/usr/bin/env python
import logging
import sys
from binance.cm_futures import CMFutures
from binance.error import ClientError, ServerError
from binance.lib.utils import config_logging

# Professional logging setup
# INFO level is cleaner for production; use DEBUG only for deep troubleshooting
config_logging(logging, logging.INFO)
logger = logging.getLogger(__name__)

def fetch_book_ticker(symbol: str):
    """
    Fetches the best price and quantity on the order book for a given symbol.
    Includes robust error handling for network and API issues.
    """
    # Initialize client - In production, use environment variables for keys
    client = CMFutures()

    try:
        # Fetching the ticker
        logger.info(f"Fetching book ticker for {symbol}...")
        ticker_data = client.book_ticker(symbol)
        
        # Structure the data for better readability and downstream processing
        processed_data = {
            "symbol": ticker_data.get("symbol"),
            "bid_price": ticker_data.get("bidPrice"),
            "ask_price": ticker_data.get("askPrice"),
            "bid_qty": ticker_data.get("bidQty"),
            "ask_qty": ticker_data.get("askQty"),
            "time": ticker_data.get("time")
        }
        
        return processed_data

    except ClientError as e:
        logger.error(f"Client error occurred: {e.error_message} (Code: {e.error_code})")
    except ServerError as e:
        logger.error(f"Server is busy or down: {e.message}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
    
    return None

if __name__ == "__main__":
    target_symbol = "BTCUSD_PERP"
    result = fetch_book_ticker(target_symbol)
    
    if result:
        print("\n--- Market Data ---")
        for key, value in result.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
    else:
        print("\nFailed to retrieve market data.")
        sys.exit(1)
