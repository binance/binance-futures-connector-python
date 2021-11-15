#!/usr/bin/env python
import logging
from binance.delivery import Delivery as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

# historical_trades requires api key in request header
client = Client(key = key)
logging.info(client.historical_trades("BTCUSD_PERP", **{"limit" : 10}))
