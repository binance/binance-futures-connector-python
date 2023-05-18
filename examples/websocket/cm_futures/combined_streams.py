import logging
import time

from binance.lib.utils import config_logging
from binance.websocket.cm_futures.websocket_client import CMFuturesWebsocketClient

config_logging(logging, logging.DEBUG)


def message_handler(_, message):
    logging.info(message)


my_client = CMFuturesWebsocketClient(on_message=message_handler, is_combined=True)


my_client.subscribe(
    stream=["btcusd_perp@ticker", "btcusd_perp@markPrice@1s"],
)

time.sleep(10)
my_client.stop()
