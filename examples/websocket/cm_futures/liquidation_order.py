#!/usr/bin/env python

import time
import logging
from binance.lib.utils import config_logging
from binance.websocket.cm_futures.websocket_client import CMFuturesWebsocketClient

config_logging(logging, logging.DEBUG)


def message_handler(_, message):
    print(message)


my_client = CMFuturesWebsocketClient(on_message=message_handler)

my_client.liquidation_order(
    symbol="btcusd_perp",
    id=13,
)

time.sleep(10)

logging.debug("closing ws connection")
my_client.stop()
