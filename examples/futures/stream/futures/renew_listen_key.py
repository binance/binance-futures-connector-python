#!/usr/bin/env python
import logging
from binance.futures import Futures as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""

client = Client(key, base_url="https://fapi.binance.com")
logging.info(client.renew_listen_key(""))
