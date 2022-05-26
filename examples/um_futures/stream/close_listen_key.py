#!/usr/bin/env python
import logging
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""

um_futures_client = UMFutures(key)
logging.info(um_futures_client.close_listen_key("the_listen_key"))
