#!/usr/bin/env python

import time
import logging
from binance.lib.utils import config_logging
from binance.websocket.cm_futures.websocket_client import CMFuturesWebsocketClient

config_logging(logging, logging.DEBUG)


def message_handler(_, message):
    print(message)


my_client = CMFuturesWebsocketClient(on_message=message_handler)

my_client.partial_book_depth(
    symbol="bnbusd_perp",
    id=1,
    level=10,
    speed=100,
)

time.sleep(2)

logging.debug("closing ws connection")
my_client.stop()
