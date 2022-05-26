#!/usr/bin/env python
from binance.delivery import Delivery as Client
import logging
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

client = Client()
logging.info(client.funding_rate("BTCUSD_PERP", **{"limit": 100}))
