# Binance Futures Public API Connector Python
[![Python 3.6](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-360/)
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

## Documentation
- USDT-M Futures: https://github.com/Binance-docs/binance-futures-connector-python/wiki/USDT-M-Futures
- COIN-M Futures: https://github.com/Binance-docs/binance-futures-connector-python/wiki/COIN-M-Futures

## RESTful APIs

Usage examples:
```python
from binance.futures import Futures 

client = Futures()
print(client.time())

client = Futures(key='<api_key>', secret='<api_secret>')

# Get account information
print(client.account())

# Post a new order
params = {
    'symbol': 'BTCUSDT',
    'side': 'SELL',
    'type': 'LIMIT',
    'timeInForce': 'GTC',
    'quantity': 0.002,
    'price': 59808
}

response = client.new_order(**params)
print(response)
```
Please find `examples` folder to check for more endpoints.

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
from binance.futures import Futures as Client

client = Client(key, secret)
response = client.query_order('BTCUSDT', orderId=11, recvWindow=10000)
```

### Timeout

`timeout` is available to be assigned with the number of seconds you find most appropriate to wait for a server response.<br/>
Please remember the value as it won't be shown in error message _no bytes have been received on the underlying socket for timeout seconds_.<br/>
By default, `timeout` is None. Hence, requests do not time out.

```python
from binance.futures import Futures as Client

client= Client(timeout=1)
```

### Response Metadata

The Binance API server provides weight usages in the headers of each response.
You can display them by initializing the client with `show_limit_usage=True`:

```python
from binance.futures import Futures as Client

client = Client(show_limit_usage=True)
print(client.time())
```
returns:

```python
{'data': {'serverTime': 1587990847650}, 'limit_usage': {'x-mbx-used-weight': '31', 'x-mbx-used-weight-1m': '31'}}
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

```python
from binance.websocket.futures.websocket_client import FuturesWebsocketClient as WebsocketClient

def message_handler(message):
    print(message)

ws_client = WebsocketClient()
ws_client.start()

ws_client.mini_ticker(
    symbol='bnbusdt',
    id=1,
    callback=message_handler,
)

# Combine selected streams
ws_client.instant_subscribe(
    stream=['bnbusdt@bookTicker', 'ethusdt@bookTicker'],
    callback=message_handler,
)

ws_client.stop()
```
More websocket examples are available in the `examples` folder

### Heartbeat

Once connected, the websocket server sends a ping frame every 3 minutes and requires a response pong frame back within
a 10 minutes period. This package handles the pong responses automatically.

