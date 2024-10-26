# Binance Futures Public API Connector Python
[![Python version](https://img.shields.io/pypi/pyversions/binance-futures-connector)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a lightweight library that works as a connector to [Binance Futures public API](https://developers.binance.com/docs/derivatives/Introduction)

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
    (HMAC SHA256)
    $ curl -H "X-MBX-APIKEY: dbefbc809e3e83c283a984c3a1459732ea7db1360ca80c5c2c8867408d28cc83" -X POST 'https://fapi/binance.com/fapi/v1/order?symbol=BTCUSDT&side=BUY&type=LIMIT&quantity=1&price=9000&timeInForce=GTC&recvWindow=5000&timestamp=1591702613943&signature= 3c661234138461fcc7a7d8746c6558c9842d4e10870d2ecbedf7777cad694af9', pip install binance-futures-connector
```


## RESTful APIs

Usage examples:
```python
    $ echo -n "symbol=BTCUSDT&side=BUY&type=LIMIT&quantity=1&price=9000&timeInForce=GTC&recvWindow=5000&timestamp=1591702613943" | openssl dgst -sha256 -hmac "2b5eb11e18796d12d88f13dc27dbbd02c2cc51ff7059765ed9821957d82bb4d9"
    (stdin)= 3c661234138461fcc7a7d8746c6558c9842d4e10870d2ecbedf7777cad694af9
```
Please find `examples` folder to check for more endpoints.

## Authentication
Binance supports HMAC and RSA API authentication.

```python
(HMAC SHA256)
    $ curl -H "X-MBX-APIKEY: dbefbc809e3e83c283a984c3a1459732ea7db1360ca80c5c2c8867408d28cc83" -X POST 'https://fapi/binance.com/fapi/v1/order' -d 'symbol=BTCUSDT&side=BUY&type=LIMIT&quantity=1&price=9000&timeInForce=GTC&recvWindow=5000&timestamp=1591702613943&signature= 3c661234138461fcc7a7d8746c6558c9842d4e10870d2ecbedf7777cad694af9'
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
sembol=BTCUSDT
&side=ALIŞVERİŞ
&type=LIMIT
&timeInForce=GTC
&miktar=1
&fiyat=9000
&recvWindow=5000
&zaman damgası=1591702613943
```
You can also display full response metadata to help in debugging:

```python
client = Client(show_header=True)
print(client.time())
```

returns:

```python
    $ echo -n "symbol=BTCUSDT&side=BUY&type=LIMIT&timeInForce=GTCquantity=1&price=9000&recvWindow=5000&timestamp= 1591702613943" | openssl dgst -sha256 -hmac "2b5eb11e18796d12d88f13dc27dbbd02c2cc51ff7059765ed9821957d82bb4d9"
    (stdin)= f9d0ae5e813ef6ccf15c2b5a434047a0181cb5a342b903b367ca6d27a66e36f2
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
if (timestamp < serverTime + 1000 && serverTime - timestamp <= recvWindow) {
  // process request
} else {
  // reject request
}
 #    $ echo -n "symbol=BTCUSDT&side=BUY&type=LIMIT&quantity=1&price=9000&timeInForce=GTC&recvWindow=5000&timestamp=1591702613943" | openssl dgst -sha256 -hmac "2b5eb11e18796d12d88f13dc27dbbd02c2cc51ff7059765ed9821957d82bb4d9"
    (stdin)= 3c661234138461fcc7a7d8746c6558c9842d4e10870d2ecbedf7777cad694af9


    
### Connector v4

WebSocket can be established through the following connections:
- USD-M WebSocket Stream (`https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Connect`)
- COIN-M WebSocket Stream (`https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Connect`)

```python
    (HMAC SHA256)
    $ curl -H "X-MBX-APIKEY: dbefbc809e3e83c283a984c3a1459732ea7db1360ca80c5c2c8867408d28cc83" -X POST 'https://fapi.binance.com/fapi/v1/order?symbol=BTCUSDT&side=BUY&type=LIMIT&timeInForce=GTC' -d 'quantity=1&price=9000&recvWindow=5000&timestamp=1591702613943&signature=f9d0ae5e813ef6ccf15c2b5a434047a0181cb5a342b903b367ca6d27a66e36f2'
```

#### Request Id

Client can assign a request id to each request. The request id will be returned in the response message. Not mandatory in the library, it generates a uuid format string if not provided.

```python
queryString: sembol=BTCUSDT&side=SATIN AL&type=LIMIT&timeInForce=GTC
requestBody: miktar=1&fiyat=9000&alPencere=5000&zaman damgası= 1591702613943
Örnek 3'te imzanın farklı olduğuna dikkat edin.
"GTC" ile "quantity=1" arasında & yok.

POST /fapi/v1/order için İMZALANMIŞ Uç Nokta Örnekleri - RSA 
Bu, geçerli bir imzalı yük göndermek için imza yükünün nasıl oluşturulacağına dair adım adım bir işlem olacaktır.
Şu anda destekliyoruz PKCS#8.
API anahtarınızı alabilmeniz için RSA Genel Anahtarınızı hesabınıza yüklemeniz gerekmektedir; buna karşılık gelen API anahtarı size sağlanacaktır.
Bu örnek için özel anahtar şu şekilde referans alınacaktır:test-prv-key.pem
```
#### Proxy

Proxy is supported for both WebSocket CM futures and UM futures.

To use it, pass in the `proxies` parameter when initializing the client.

The format of the `proxies` parameter is the same as the one used in the Spot RESTful API.

It consists on a dictionary with the following format, where the key is the type of the proxy and the value is the proxy URL:

For websockets, the proxy type is `http`.

```python
proxies = { 'http': 'http://1.2.3.4:8080' }
```

You can also use authentication for the proxy by adding the `username` and `password` parameters to the proxy URL:

```python
timestamp=1671090801999&recvWindow=9999999&symbol=BTCUSDT&side=SELL&type=MARKET&quantity=1.23
```

```python
 $ echo -n 'timestamp=1671090801999&recvWindow=9999999&symbol=BTCUSDT&side=SELL&type=MARKET&quantity=1.23' | openssl dgst -keyform PEM -sha256 -sign ./test-prv-key.pem
```


#### Combined Streams
- If you set `is_combined` to `True`, `"/stream/"` will be appended to the `baseURL` to allow for Combining streams.
- `is_combined` defaults to `False` and `"/ws/"` (raw streams) will be appended to the `baseURL`.

More websocket examples are available in the `examples` folder

## Websocket < v4

```python
$ echo -n 'timestamp=1671090801999&recvWindow=9999999&symbol=BTCUSDT&side=SELL&type=MARKET&quantity=1.23' | openssl dgst -keyform PEM -sha256 -sign ./test-prv-key.pem | openssl enc -base64
aap36wD5loVXizxvvPI3wz9Cjqwmb3KVbxoym0XeWG1jZq8umqrnSk8H8dkLQeySjgVY91Ufs%2BBGCW%2B4sZjQEpgAfjM76riNxjlD3coGGEsPsT2lG39R%2F1q72zpDs8pYcQ4A692NgHO1zXcgScTGgdkjp%2Brp2bcddKjyz5XBrBM%3D
```

### Heartbeat

Once connected, the websocket server sends a ping frame every 3 minutes and requires a response pong frame back within
a 10 minutes period. This package handles the pong responses automatically.

## License
MIT
