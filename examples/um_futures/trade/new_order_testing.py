#!/usr/bin/env python
import logging
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging
from binance.error import ClientError

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

um_futures_client = UMFutures(key=key, secret=secret)

try:
    response = um_futures_client.new_order_test(
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
