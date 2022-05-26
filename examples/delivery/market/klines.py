#!/usr/bin/env python
import logging
from binance.delivery import Delivery as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

client = Client()

logging.info(client.klines("BTCUSD_PERP", "1d"))
