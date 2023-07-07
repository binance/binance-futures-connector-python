#!/usr/bin/env python

import logging
import time
from binance.lib.utils import config_logging
from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient

config_logging(logging, logging.DEBUG)


def message_handler(_, message):
    logging.info(message)


proxy = {'host': '192.168.5.121', 'port': 7890}
my_client = UMFuturesWebsocketClient(on_message=message_handler, is_combined=True, proxy=proxy)

# Subscribe to a single symbol stream
my_client.agg_trade(symbol="bnbusdt")

time.sleep(5)

# Unsubscribe
my_client.agg_trade(
    symbol="bnbusdt", action=UMFuturesWebsocketClient.ACTION_UNSUBSCRIBE
)

time.sleep(5)

logging.info("closing ws connection")
my_client.stop()
