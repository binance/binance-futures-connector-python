#!/usr/bin/env python
import logging
from binance.futures import Futures as Client
from binance.lib.utils import config_logging
from binance.error import ClientError

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

client = Client(key, secret, base_url="https://fapi.binance.com")

try:
    response = client.new_order_test(
        symbol="BTCUSDT",
        side="SELL",
        type="LIMIT",
        quantity=0.001,
        timeInForce="GTC",
        price=59808.02,
    )
    logging.info(response)
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
