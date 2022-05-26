#!/usr/bin/env python
import logging
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

um_futures_client = UMFutures()

logging.info(um_futures_client.index_price_klines("BTCUSDT", "1d", **{"limit": 500}))
