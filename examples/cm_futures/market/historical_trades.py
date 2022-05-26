#!/usr/bin/env python
import logging
from binance.cm_futures import CMFutures
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""

# historical_trades requires api key in request header
cm_futures_client = CMFutures(key=key)
logging.info(cm_futures_client.historical_trades("BTCUSD_PERP", **{"limit": 10}))
