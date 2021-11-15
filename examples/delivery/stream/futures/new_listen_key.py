#!/usr/bin/env python
import logging
from binance.delivery import Delivery as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""

client = Client(key, base_url="https://dapi.binance.com")
logging.info(client.new_listen_key())
