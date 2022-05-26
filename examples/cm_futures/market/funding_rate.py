#!/usr/bin/env python
from binance.cm_futures import CMFutures
import logging
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

cm_futures_client = CMFutures()
logging.info(cm_futures_client.funding_rate("BTCUSD_PERP", **{"limit": 100}))
