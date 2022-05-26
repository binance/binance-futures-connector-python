#!/usr/bin/env python
import logging
from binance.futures import Futures as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

# historical_trades requires api key in request header
futures_client = Client(key=key)
logging.info(futures_client.historical_trades("BTCUSDT", **{"limit": 10}))
