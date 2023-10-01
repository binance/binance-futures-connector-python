# Langsung ke konten utama
GOOGLEFINANCE
Mengambil informasi sekuritas saat ini atau terdahulu dari Google Finance.

Contoh Penggunaan
GOOGLEFINANCE("NASDAQ:GOOG", "harga", TANGGAL(2014,1,1), TANGGAL(2014,12,31), "HARIAN")

GOOGLEFINANCE("NASDAQ:GOOG","harga",HARI INI()-30,HARI INI())

GOOGLEFINANCE(A2,A3)

Sintaks
GOOGLEFINANCE(ticker, [attribute], [start_date], [end_date|num_days], [interval])

ticker - Simbol ticker untuk sekuritas yang akan dipertimbangkan. Untuk hasil yang akurat dan menghindari perbedaan, Diwajibkan untuk menggunakan keduanya, baik simbol bursa dan simbol ticker. Misalnya, gunakan “NASDAQ:GOOG”, bukan “GOOG”.

Jika simbol bursa tidak ditentukan, GOOGLEFINANCE akan menggunakan penilaian terbaiknya guna memilih salah satunya untuk Anda.

Kode Instrumen Reuters tidak lagi didukung. Gunakan TSE:123 atau ASX:XYZ, bukan ticker 123.TO atau XYZ.AX.

Tidak semua fitur didukung untuk saat ini.

attribute - [ OPTIONAL - "price" secara default ] - Atribut yang akan diambil terkait ticker dari Google Finance dan diperlukan jika tanggal ditentukan.

attribute adalah salah satu dari hal berikut untuk data real-time:

"price" - Penawaran harga real-time, tertunda hingga 20 menit.

"priceopen" - Harga saat pasar buka.

"high" - Harga tinggi ini hari.

"low" - Harga rendah hari ini.

"volume" - Volume perdagangan hari ini.

"marketcap" - Kapitalisasi pasar saham.

"tradetime" - Waktu trading terakhir.

"datadelay" - Seberapa jauh data real-time tertunda.

"volumeavg" - Volume rata-rata trading harian.

"pe" - Rasio harga/laba.

"eps" - Laba per saham.

"high52" - Harga tinggi 52 minggu.

"low52" - Harga rendah 52 minggu.

"change" - Perubahan harga sejak penutupan hari perdagangan sebelumnya.

"beta" - Nilai beta.

"changepct" - Persentase perubahan harga sejak penutupan hari perdagangan sebelumnya.

"closeyest" - harga penutupan hari sebelumnya.

"shares" - Jumlah saham yang beredar.

"currency" - Mata uang yang digunakan untuk menetapkan harga sekuritas. Mata uang tidak memiliki jendela perdagangan, sehingga open, low, high, dan volume tidak akan ditampilkan untuk argumen ini.

attribute untuk data historis adalah salah satu dari berikut ini:

"open" - Harga pembukaan untuk tanggal yang ditentukan.

"close" - Harga penutupan untuk tanggal yang ditentukan.

"high" - Harga tinggi untuk tanggal yang ditentukan.

"low" - Harga rendah untuk tanggal yang ditentukan.

"volume" - Volume untuk tanggal yang ditentukan.

"all" - Semua yang disebutkan di atas.

attribute untuk data reksadana adalah salah satu dari berikut ini:

"closeyest" - harga penutupan hari sebelumnya.

"date" - Tanggal saat nilai aktiva bersih dilaporkan.

"returnytd" - Tahun ke tanggal pengembalian.

"netassets" - Aktiva bersih.

"change" - Perubahan pada nilai aktiva bersih yang terakhir dilaporkan dan sebelumnya.

"changepct" - Perubahan persentase pada nilai aktiva bersih.

"yieldpct" - Hasil distribusi, jumlah distribusi pendapatan 12 bulan sebelumnya (dividen saham dan pembayaran bunga pendapatan tetap) dan keuntungan nilai aktiva bersih dibagi dengan jumlah nilai aktiva bersih bulan sebelumnya.

"returnday" - Total pengembalian satu hari.

"return1" - Total pengembalian satu minggu.

"return4" - Total pengembalian empat minggu.

"return13" - Total pengembalian tiga belas minggu.

"return52" - Total pengembalian lima puluh dua minggu (tahunan).

"return156" - Total pengembalian 156 minggu (3 tahun).

"return260" - Total pengembalian 260 minggu (5 tahun).

"incomedividend" - Jumlah distribusi tunai baru-baru ini.

"incomedividenddate" - Tanggal distribusi tunai baru-baru ini.

"capitalgain" - Jumlah distribusi keuntungan modal baru-baru ini.

"morningstarrating" - Peringkat "bintang" Morningstar.

"expenseratio" - Rasio beban dana.

start_date - [ OPTIONAL ] - Tanggal awal saat mengambil data historis.

Jika start_date ditentukan namun end_date|num_days tidak ditentukan, hanya data satu hari yang dikembalikan.
end_date|num_days - [ OPSIONAL ] - Tanggal akhir saat mengambil data historis, atau jumlah hari dari start_date yang ingin ditampilkan datanya.

interval - [ OPSIONAL ] - Frekuensi data yang ditampilkan; "DAILY" atau "WEEKLY".

interval juga dapat ditentukan sebagai 1 atau 7. Nilai numerik lainnya tidak diizinkan.
Catatan
Batasan penggunaan: Data ini bukan untuk penggunaan profesional industri keuangan atau digunakan oleh profesional lain di perusahaan non-keuangan (termasuk entitas pemerintah). Penggunaan profesional dapat dikenakan biaya lisensi tambahan dari penyedia data pihak ketiga.

Semua parameter harus diapit tanda kutip atau menjadi referensi bagi sel yang berisi teks. 
Penting: Pengecualian mungkin terjadi saat interval ditentukan sebagai angka dan saat end_date|num_days ditentukan sebagai jumlah hari.

Hasil real-time akan ditampilkan sebagai nilai dalam satu sel. Data historis, bahkan untuk satu hari, akan ditampilkan sebagai array yang diluaskan dengan judul kolom.

Beberapa atribut mungkin tidak memberikan hasil untuk semua simbol.

Jika ada parameter tanggal yang ditentukan, permintaan dianggap historis dan hanya atribut historis yang diizinkan.
GOOGLEFINANCE hanya tersedia dalam bahasa Inggris dan tidak mendukung sebagian besar bursa internasional.

Data historis tidak dapat didownload atau diakses melalui Sheets API atau Apps Script. Jika mencoba untuk melakukannya, Anda akan melihat error #N/A menggantikan nilai dalam sel yang sesuai pada spreadsheet.

Harga tidak berasal dari semua pasar dan mungkin tertunda hingga 20 menit. Informasi disediakan 'sebagaimana adanya' dan semata-mata hanya sebagai informasi, serta bukan untuk tujuan trading atau sebagai saran.

Google memperlakukan tanggal yang diteruskan ke GOOGLEFINance sebagai siang hari dalam waktu UTC. Bursa yang tutup sebelum waktu itu dapat digeser selama satu hari.

Contoh
Buat salinan

Catatan: Setiap contoh ditampilkan dalam tab terpisah.

Penggunaan umum
Mengambil informasi pasar dari Google Finance.


 

Atribut umum

 

Data pasar historis
Mengambil informasi pasar historis berdasarkan tanggal yang ditentukan dari Google Finance.


 

Reksadana
Atribut umum untuk reksadana.


 

Tren bursa mata uang
Membuat diagram di dalam sel untuk menampilkan tren bursa mata uang selama 30 hari terakhir, menggunakan hasil pengambilan yang ditampilkan oleh GoogleFinance.



Beri masukan tentang artikel ini

Google
Daftar fungsi Google Spreadsheet
ARRAYFORMULA
DETECTLANGUAGE
GOOGLEFINANCE
GOOGLETRANSLATE
IMAGE
Fungsi QUERY
SPARKLINE
Membuat & menggunakan fungsi bernama
Fungsi LAMBDA
""
Visit the Learning Center
Using Google products, like Google Docs, at work or school? Try powerful tips, tutorials, and templates. Learn to work on Office files without installing Office, create dynamic project plans and team calendars, auto-organize your inbox, and more.

# Función CODIFICAR URL
Codifica texto para que pueda usarse en la cadena de consulta de una URL.

Partes de una función ENCODEURL
ENCODEURL(text)

Parte	Descripción
text	El texto que se codificará como una URL.
Fórmulas de muestra
ENCODEURL(“hello world!”)

ENCODEURL(A10)

Notas
Esta función es útil para pasar argumentos de URL a funciones que realizan solicitudes web, como IMPORTHTML.

Ejemplos
Codifica el texto "¡Hola, mundo!" en un formato compatible con URL.

 	A	B
1	Fórmula	Resultado
2	=ENCODEURL(“¡hola mundo!”)	hola%2C%20mundo%21
 

Utilice ENCODEURL para crear un hipervínculo. 

 	A	B
1	Fórmula	Resultado
2	=HIPERVÍNCULO("http://google.com?q=" & ENCODEURL("hola mundo"))	http://google.com?q=hola%20world
Funciones relacionadas
IMPORTHTML : importa datos de una tabla o lista dentro de una página HTML.
CLEAN : Devuelve el texto sin los caracteres ASCII no imprimibles.
REEMPLAZAR : Reemplaza parte de una cadena de texto con una cadena de texto diferente.

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

# HIPERVÍNCULO
Crea un hipervínculo dentro de una celda.

Uso de muestra
HYPERLINK("http://www.google.com/","Google")

Sintaxis
HYPERLINK(url, [link_label])

url- La URL completa de la ubicación del enlace entre comillas, o una referencia a una celda que contenga dicha URL.

Sólo se permiten ciertos tipos de enlaces. http://, https://, mailto:, aim:, ftp://, gopher://, telnet://, y news://están permitidos; otros están explícitamente prohibidos. Si se especifica otro protocolo, link_labelse mostrará en la celda, pero no tendrá un hipervínculo.

Si no se especifica ningún protocolo, http://se supone y se antepone a url.

link_label- [ OPCIONAL: urlde forma predeterminada ] : el texto que se mostrará en la celda como enlace, entre comillas, o una referencia a una celda que contenga dicha etiqueta.

Si link_labeles una referencia a una celda vacía, urlse mostrará como un enlace si es válido o como texto sin formato en caso contrario.

Si link_labeles el literal de cadena vacío (""), la celda aparecerá vacía, pero aún se podrá acceder al enlace haciendo clic o moviéndose a la celda.

Notas
Si no se incluye url(o link_label, si se proporciona) entre comillas, se producirá un error.

Google Sheets convierte automáticamente la mayoría de los tipos de URL válidos cuando se escriben en una celda sin necesidad de utilizar esta función.

Ejemplos
Crea un hipervínculo dentro de la celda para el objeto especificado cell_text.



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
proxies = { 'http': 'http://username:password@host:port' }
```

```python
# WebSocket Stream Client
import time
from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient

proxies = {'http': 'http://1.2.3.4:8080'}

def message_handler(_, message):
    logging.info(message)

my_client = UMFuturesWebsocketClient(on_message=message_handler, proxies=proxies)

# Subscribe to a single symbol stream
my_client.agg_trade(symbol="bnbusdt")
time.sleep(5)
logging.info("closing ws connection")
my_client.stop()
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
