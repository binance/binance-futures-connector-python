import logging
import time

from binance.lib.utils import config_logging
from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient

config_logging(logging, logging.DEBUG)


def message_handler(_, message):
    logging.info(message)


my_client = UMFuturesWebsocketClient(on_message=message_handler, is_combined=True)


my_client.subscribe(
    stream=["bnbusdt@bookTicker", "ethusdt@bookTicker"],
)

time.sleep(10)
my_client.stop()
