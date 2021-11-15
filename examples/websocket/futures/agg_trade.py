#!/usr/bin/env python
import sys
sys.path.insert(0,'/Users/tenghuang/Desktop/binance-futures-connector-python/')

import time
import logging
from binance.lib.utils import config_logging
from binance.websocket.futures.websocket_client import FuturesWebsocketClient as Client

config_logging(logging, logging.DEBUG)


def message_handler(message):
    print(message)


my_client = Client()
my_client.start()

my_client.agg_trade(
    symbol="btcusdt",
    id=1,
    callback=message_handler,
)

time.sleep(2)

my_client.agg_trade(
    symbol="ethusdt",
    id=1,
    callback=message_handler,
)

logging.debug("closing ws connection")
my_client.stop()
