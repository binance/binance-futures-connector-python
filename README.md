# Binance Futures Public API Connector Python
[![Python version](https://img.shields.io/pypi/pyversions/binance-futures-connector)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a lightweight library that works as a connector to [Binance Futures public API](https://binance-docs.github.io/apidocs/futures/en/)

- Supported APIs:
    - USDT-M Futures `/fapi/*`
    - COIN-M Delivery `/dapi/*`
    - Futures/Delivery Websocket Market Stream
    - Futures/Delivery User Data Stream
- Inclusion of examples
- Customizable base URL, request timeout
- Response metadata can be displayed

## Installation

```bash
pip install binance-futures-connector
```


## RESTful APIs

Usage examples:
```python

from binance.cm_futures import CMFutures

cm_futures_client = CMFutures()

# get server time
print(cm_futures_client.time())

cm_futures_client = CMFutures(key='<api_key>', secret='<api_secret>')

# Get account information
print(cm_futures_client.account())

# Post a new order
params = {
    'symbol': 'BTCUSDT',
    'side': 'SELL',
    'type': 'LIMIT',
    'timeInForce': 'GTC',
    'quantity': 0.002,
    'price': 59808
}

response = cm_futures_client.new_order(**params)
print(response)
```
Please find `examples` folder to check for more endpoints.

## Authentication
Binance supports HMAC and RSA API authentication.

```python
# HMAC Authentication
client = Client(api_key, api_secret)
print(client.account())

# RSA Authentication
key = ""
with open("/Users/john/private_key.pem", "r") as f: # Location of private key file
    private_key = f.read()
private_key_passphrase = "" # Optional: only used for encrypted RSA key

client = Client(key=key, private_key=private_key, private_key_passphrase=private_key_passphrase)
print(client.account())
```
Please see `examples/um_futures/trade/get_account.py` or `examples/cm_futures/trade/get_account.py` for more details.

### Base URL

For USDT-M Futures, if `base_url` is not provided, it defaults to `fapi.binance.com`.<br/>
For COIN-M Delivery, if `base_url` is not provided, it defaults to `dapi.binance.com`.<br/>
It's recommended to pass in the `base_url` parameter, even in production as Binance provides alternative URLs

### Optional parameters

PEP8 suggests _lowercase with words separated by underscores_, but for this connector,
the methods' optional parameters should follow their exact naming as in the API documentation.

```python
# Recognised parameter name
response = client.query_order('BTCUSDT', orderListId=1)

# Unrecognised parameter name
response = client.query_order('BTCUSDT', order_list_id=1)
```

### RecvWindow parameter

Additional parameter `recvWindow` is available for endpoints requiring signature.<br/>
It defaults to `5000` (milliseconds) and can be any value lower than `60000`(milliseconds).
Anything beyond the limit will result in an error response from Binance server.

```python
from binance.cm_futures import CMFutures

cm_futures_client = CMFutures(key='<api_key>', secret='<api_secret>')
response = cm_futures_client.query_order('BTCUSDT', orderId=11, recvWindow=10000)
```

### Timeout

`timeout` is available to be assigned with the number of seconds you find most appropriate to wait for a server response.<br/>
Please remember the value as it won't be shown in error message _no bytes have been received on the underlying socket for timeout seconds_.<br/>
By default, `timeout` is None. Hence, requests do not time out.

```python
from binance.cm_futures import CMFutures

client= CMFutures(timeout=1)
```

### Proxy
proxy is supported

```python
from binance.cm_futures import CMFutures

proxies = { 'https': 'http://1.2.3.4:8080' }

client= CMFutures(proxies=proxies)
```

### Response Metadata

The Binance API server provides weight usages in the headers of each response.
You can display them by initializing the client with `show_limit_usage=True`:

```python
from binance.cm_futures import CMFutures

client = CMFutures(show_limit_usage=True)
print(client.time())
```
returns:

```python
{'limit_usage': {'x-mbx-used-weight-1m': '1'}, 'data': {'serverTime': 1653563092778}}
```
You can also display full response metadata to help in debugging:

```python
client = Client(show_header=True)
print(client.time())
```

returns:

```python
{'data': {'serverTime': 1587990847650}, 'header': {'Context-Type': 'application/json;charset=utf-8', ...}}
```

If `ClientError` is received, it'll display full response meta information.

### Display logs

Setting the log level to `DEBUG` will log the request URL, payload and response text.

### Error

There are 2 types of error returned from the library:
- `binance.error.ClientError`
    - This is thrown when server returns `4XX`, it's an issue from client side.
    - It has 4 properties:
        - `status_code` - HTTP status code
        - `error_code` - Server's error code, e.g. `-1102`
        - `error_message` - Server's error message, e.g. `Unknown order sent.`
        - `header` - Full response header.
- `binance.error.ServerError`
    - This is thrown when server returns `5XX`, it's an issue from server side.

## Websocket

### Connector v4

WebSocket can be established through the following connections:
- USD-M WebSocket Stream (`https://binance-docs.github.io/apidocs/futures/en/#websocket-market-streams`)
- COIN-M WebSocket Stream (`https://binance-docs.github.io/apidocs/delivery/en/#websocket-market-streams`)

```python
# WebSocket Stream Client
import time
from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient

def message_handler(_, message):
    logging.info(message)

my_client = UMFuturesWebsocketClient(on_message=message_handler)

# Subscribe to a single symbol stream
my_client.agg_trade(symbol="bnbusdt")
time.sleep(5)
logging.info("closing ws connection")
my_client.stop()
```

#### Request Id

Client can assign a request id to each request. The request id will be returned in the response message. Not mandatory in the library, it generates a uuid format string if not provided.

```python
# id provided by client
my_client.agg_trade(symbol="bnbusdt", id="my_request_id")

# library will generate a random uuid string
my_client.agg_trade(symbol="bnbusdt")
```

#### Combined Streams
- If you set `is_combined` to `True`, `"/stream/"` will be appended to the `baseURL` to allow for Combining streams.
- `is_combined` defaults to `False` and `"/ws/"` (raw streams) will be appended to the `baseURL`.

More websocket examples are available in the `examples` folder

## Websocket < v4

```python
import time
from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient

def message_handler(message):
    print(message)

my_client = UMFuturesWebsocketClient(on_message=message_handler)

# Subscribe to a single symbol stream
my_client.agg_trade(symbol="bnbusdt")
time.sleep(5)
print("closing ws connection")
my_client.stop()

```

### Heartbeat

Once connected, the websocket server sends a ping frame every 3 minutes and requires a response pong frame back within
a 10 minutes period. This package handles the pong responses automatically.

## License
MIT
