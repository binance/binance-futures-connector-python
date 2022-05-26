#!/usr/bin/env python
import logging
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

um_futures_client = UMFutures()

logging.info(
    um_futures_client.top_long_short_position_ratio("BTCUSDT", "1h", **{"limit": 30})
)
