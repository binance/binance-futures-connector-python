#!/usr/bin/env python
from binance.um_futures import UMFutures
import logging
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

um_futures_client = UMFutures()
logging.info(um_futures_client.funding_rate("BTCUSDT", **{"limit": 100}))
