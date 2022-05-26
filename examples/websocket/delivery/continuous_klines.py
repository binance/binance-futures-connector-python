#!/usr/bin/env python

import time
import logging
from binance.lib.utils import config_logging
from binance.websocket.delivery.websocket_client import (
    DeliveryWebsocketClient as Client,
)

config_logging(logging, logging.DEBUG)


def message_handler(message):
    print(message)


my_client = Client()
my_client.start()

my_client.continuous_kline(
    pair="btcusd",
    id=1,
    contractType="PERPETUAL",
    interval="1m",
    callback=message_handler,
)

time.sleep(10)

logging.debug("closing ws connection")
my_client.stop()
