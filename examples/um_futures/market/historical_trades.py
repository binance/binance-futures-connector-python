#!/usr/bin/env python
import logging
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""

# historical_trades requires api key in request header
um_futures_client = UMFutures(key=key)

logging.info(um_futures_client.historical_trades("BTCUSDT", **{"limit": 10}))
