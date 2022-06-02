#!/usr/bin/env python
import logging
from binance.cm_futures import CMFutures as Client
from binance.lib.utils import config_logging
from binance.error import ClientError

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

client = Client(key, secret, base_url="https://dapi.binance.com")

params = [
    {
        "symbol": "BTCUSD_PERP",
        "side": "BUY",
        "type": "LIMIT",
        "quantity": "0.001",
        "timeInForce": "GTC",
        "price": "60000.1",
    }
]

try:
    response = client.new_batch_order(params)
    logging.info(response)
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
