#!/usr/bin/env python
import logging
from binance.cm_futures import CMFutures
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""

cm_futures_client = CMFutures(key=key)

logging.info(cm_futures_client.close_listen_key("the_listen_key"))
