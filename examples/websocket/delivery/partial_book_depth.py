#!/usr/bin/env python

import time
import logging
from binance.lib.utils import config_logging
from binance.websocket.delivery.websocket_client import DeliveryWebsocketClient as Client

config_logging(logging, logging.DEBUG)


def message_handler(message):
    print(message)


my_client = Client()
my_client.start()

my_client.partial_book_depth(
    symbol="bnbusd_perp",
    id=1,
    level=10,
    speed=100,
    callback=message_handler,
)

time.sleep(2)

logging.debug("closing ws connection")
my_client.stop()
