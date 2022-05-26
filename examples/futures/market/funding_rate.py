#!/usr/bin/env python
from binance.futures import Futures as Client
import logging
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

futures_client = Client()
logging.info(futures_client.funding_rate("BTCUSDT", **{"limit": 100}))
