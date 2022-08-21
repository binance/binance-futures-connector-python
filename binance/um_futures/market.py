from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters


def ping(self):
    """
    |
    | **Test Connectivity**
    | *Test connectivity to the Rest API.*

    :API endpoint: ``GET /fapi/v1/ping``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#test-connectivity
    |
    """

    url_path = "/fapi/v1/ping"
    return self.query(url_path)


def time(self):
    """
    |
    | **Check Server Time**
    | *Test connectivity to the Rest API and get the current server time.*

    :API endpoint: ``GET /fapi/v1/time``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#check-server-time
    |
    """

    url_path = "/fapi/v1/time"
    return self.query(url_path)


def exchange_info(self):
    """
    |
    | **Exchange Information**
    | *Current exchange trading rules and symbol information.*

    :API endpoint: ``GET /fapi/v1/exchangeInfo``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#exchange-information
    |
    """

    url_path = "/fapi/v1/exchangeInfo"
    return self.query(url_path)


def depth(self, symbol: str, **kwargs):
    """
    |
    | **Get Orderbook**

    :API endpoint: ``GET /fapi/v1/depth``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#order-book

    :parameter symbol: string; the trading symbol.
    :parameter limit: optional int; limit the results. Default 500, valid limits: [5, 10, 20, 50, 100, 500, 1000].
    |
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.query("/fapi/v1/depth", params)


def trades(self, symbol: str, **kwargs):
    """
    |
    | **Get Recent Market Trades**

    :API endpoint: ``GET /fapi/v1/trades``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#recent-trades-list

    :parameter symbol: string; the trading symbol.
    :parameter limit: optional int; limit the results. Default 500, max 1000.
    |
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.query("/fapi/v1/trades", params)


def historical_trades(self, symbol: str, **kwargs):
    """
    |
    | **Old Trade Lookup**
    | *Get older market historical trades.*

    :API endpoint: ``GET /fapi/v1/historicalTrades``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#old-trades-lookup-market_data

    :parameter symbol: string; the trading symbol.
    :parameter limit: optional int; limit the results. Default 500, max 1000.
    :parameter formId: optional int; trade ID to fetch from. Default gets most recent trades.
    |
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.limit_request("GET", "/fapi/v1/historicalTrades", params)


def agg_trades(self, symbol: str, **kwargs):
    """
    |
    | **Compressed/Aggregate Trades List**
    | *Get compressed, aggregate market trades. Market trades that fill at the time, from the same order, with the same price will have the quantity aggregated.*

    :API endpoint: ``GET /fapi/v1/aggTrades``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#compressed-aggregate-trades-list

    :parameter symbol: string; the trading symbol.
    :parameter limit: optional int; limit the results. Default 500, max 1000.
    :parameter formId: optional int; ID to get aggregate trades from INCLUSIVE.
    :parameter startTime: optional int; timestamp in ms to get aggregate trades from INCLUSIVE.
    :parameter endTime: optional int; timestamp in ms to get aggregate trades from INCLUSIVE.
    |
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.query("/fapi/v1/aggTrades", params)


def klines(self, symbol: str, interval: str, **kwargs):
    """
    |
    | **Kline/Candlestick Data**
    | *Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.*

    :API endpoint: ``GET /fapi/v1/klines``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#kline-candlestick-data

    :parameter symbol: string; the trading symbol.
    :parameter interval: string; the interval of kline, e.g 1m, 5m, 1h, 1d, etc. (see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info)
    :parameter limit: optional int; limit the results. Default 500, max 1000.
    :parameter startTime: optional int
    :parameter endTime: optional int
    |
    """

    check_required_parameters([[symbol, "symbol"], [interval, "interval"]])
    params = {"symbol": symbol, "interval": interval, **kwargs}
    return self.query("/fapi/v1/klines", params)


def continuous_klines(self, pair: str, contractType: str, interval: str, **kwargs):
    """
    |
    | **Continuous Kline/Candlestick Data**
    | *Kline/candlestick bars for a specific contract type. Klines are uniquely identified by their open time.*

    :API endpoint: ``GET /fapi/v1/continuousKlines``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#continuous-contract-kline-candlestick-data

    :parameter pair: string; the trading pair.
    :parameter contractType: string; PERPETUAL, CURRENT_MONTH, NEXT_MONTH, CURRENT_QUARTER, NEXT_QUARTER.
    :parameter interval: string; the interval of kline, e.g 1m, 5m, 1h, 1d, etc. (see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info)
    :parameter limit: optional int; limit the results. Default 500, max 1000.
    :parameter startTime: optional int
    :parameter endTime: optional int
    |
    """

    check_required_parameters(
        [[pair, "pair"], [contractType, "contractType"], [interval, "interval"]]
    )
    params = {
        "pair": pair,
        "contractType": contractType,
        "interval": interval,
        **kwargs,
    }
    return self.query("/fapi/v1/continuousKlines", params)


def index_price_klines(self, pair: str, interval: str, **kwargs):
    """
    |
    | **Kline/Candlestick Data for the index price of a pair.**
    | *Klines are uniquely identified by their open time.*

    :API endpoint: ``GET /fapi/v1/indexPriceKlines``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#index-price-kline-candlestick-data

    :parameter pair: string; the trading pair.
    :parameter interval: string; the interval of kline, e.g 1m, 5m, 1h, 1d, etc. (see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info)
    :parameter limit: optional int; limit the results. Default 500, max 1000.
    :parameter startTime: optional int
    :parameter endTime: optional int
    |
    """

    check_required_parameters([[pair, "pair"], [interval, "interval"]])
    params = {"pair": pair, "interval": interval, **kwargs}
    return self.query("/fapi/v1/indexPriceKlines", params)


def mark_price_klines(self, symbol: str, interval: str, **kwargs):
    """
    |
    | **Kline/candlestick bars for the mark price of a symbol.**
    | *Klines are uniquely identified by their open time.*

    :API endpoint: ``GET /fapi/v1/markPriceKlines``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#mark-price-kline-candlestick-data

    :parameter symbol: string; the trading symbol.
    :parameter interval: string; the interval of kline, e.g 1m, 5m, 1h, 1d, etc. (see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info)
    :parameter limit: optional int; limit the results. Default 500, max 1000.
    :parameter startTime: optional int
    :parameter endTime: optional int
    |
    """

    check_required_parameters([[symbol, "symbol"], [interval, "interval"]])
    params = {"symbol": symbol, "interval": interval, **kwargs}
    return self.query("/fapi/v1/markPriceKlines", params)


def mark_price(self, symbol: str=None):
    """
    |
    | **Mark Price and Funding Rate**

    :API endpoint: ``GET /fapi/v1/premiumIndex``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#mark-price

    :parameter symbol: string; the trading symbol.
    |
    """

    # check_required_parameter(symbol, "symbol")
    params = {
        "symbol": symbol,
    }
    return self.query("/fapi/v1/premiumIndex", params)


def funding_rate(self, symbol: str, **kwargs):
    """
    |
    | **Funding Rate History

    :API endpoint: ``GET /fapi/v1/fundingRate``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#get-funding-rate-history

    :parameter symbol: string; the trading symbol.
    :parameter limit: optional int; limit the results. Default 500, max 1000.
    :parameter startTime: optional int
    :parameter endTime: optional int

    **Notes**
        - If startTime and endTime are not sent, the most recent limit datas are returned.
        - If the number of data between startTime and endTime is larger than limit, return as startTime + limit.
        - In ascending order.
    |
    """

    params = {"symbol": symbol, **kwargs}
    return self.query("/fapi/v1/fundingRate", params)


def ticker_24hr_price_change(self, symbol: str = None):
    """
    |
    | **24 hour rolling window price change statistics.**
    | *Careful when accessing this with no symbol.*
    | *If the symbol is not sent, tickers for all symbols will be returned in an array.*

    :API endpoint: ``GET /fapi/v1/ticker/24hr``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#24hr-ticker-price-change-statistics

    :parameter symbol: string; the trading symbol.
    |
    """

    params = {
        "symbol": symbol,
    }
    return self.query("/fapi/v1/ticker/24hr", params)


def ticker_price(self, symbol: str = None):
    """
    |
    | **Latest price for a symbol or symbols.**

    :API endpoint: ``GET /fapi/v1/ticker/price``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#symbol-price-ticker

    :parameter symbol: optional string; the trading symbol.

    **Notes**
        - If the symbol is not sent, prices for all symbols will be returned in an array.
    |
    """

    params = {
        "symbol": symbol,
    }
    return self.query("/fapi/v1/ticker/price", params)


def book_ticker(self, symbol: str = None):
    """
    |
    | **Best price/qty on the order book for a symbol or symbols.**

    :API endpoint: ``GET /fapi/v1/ticker/bookTicker``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#symbol-order-book-ticker

    :parameter symbol: optional string; the trading symbol.

    **Notes**
        - If the symbol is not sent, bookTickers for all symbols will be returned in an array.
    |
    """

    params = {
        "symbol": symbol,
    }
    return self.query("/fapi/v1/ticker/bookTicker", params)


def open_interest(self, symbol: str):
    """
    |
    | **Get present open interest of a specific symbol.**

    :API endpoint: ``GET /fapi/v1/openInterest``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#open-interest

    :parameter symbol: string; the trading symbol.
    |
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol}
    return self.query("/fapi/v1/openInterest", params)


def open_interest_hist(self, symbol: str, period: str, **kwargs):
    """
    |
    | **Get historical open interest of a specific symbol.**

    :API endpoint: ``GET /futures/data/openInterestHist``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#open-interest-statistics

    :parameter symbol: string; the trading symbol.
    :parameter period: string; the period of open interest, "5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d".
    :parameter limit: optional int; limit the results. Default 30, max 500.
    :parameter startTime: optional int
    :parameter endTime: optional int

    **Notes**
        - If startTime and endTime are not sent, the most recent data is returned.
        - Only the data of the latest 30 days is available.
    |
    """

    check_required_parameters([[symbol, "symbol"], [period, "period"]])
    params = {"symbol": symbol, "period": period, **kwargs}
    return self.query("/futures/data/openInterestHist", params)


def top_long_short_position_ratio(self, symbol: str, period: str, **kwargs):
    """
    |
    | **Get top long short position ratio.**

    :API endpoint: ``GET /futures/data/topLongShortPositionRatio``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#top-trader-long-short-ratio-positions

    :parameter symbol: string; the trading symbol.
    :parameter period: string; the period of open interest, "5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d". (see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info)
    :parameter limit: optional int; limit the results. Default 30, max 500.
    :parameter startTime: optional int
    :parameter endTime: optional int

    **Notes**
        - If startTime and endTime are not sent, the most recent data is returned.
        - Only the data of the latest 30 days is available.
    |
    """

    check_required_parameters([[symbol, "symbol"], [period, "period"]])
    params = {"symbol": symbol, "period": period, **kwargs}
    return self.query("/futures/data/topLongShortPositionRatio", params)


def long_short_account_ratio(self, symbol: str, period: str, **kwargs):
    """
    |
    | **Get top long short account ratio.**

    :API endpoint: ``GET /futures/data/globalLongShortAccountRatio``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#long-short-ratio

    :parameter symbol: string; the trading symbol.
    :parameter period: string; the period of open interest, "5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d". (see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info)
    :parameter limit: optional int; limit the results. Default 30, max 500.
    :parameter startTime: optional int
    :parameter endTime: optional int

    **Notes**
        - If startTime and endTime are not sent, the most recent data is returned.
        - Only the data of the latest 30 days is available.
    |
    """

    check_required_parameters([[symbol, "symbol"], [period, "period"]])
    params = {"symbol": symbol, "period": period, **kwargs}
    return self.query("/futures/data/globalLongShortAccountRatio", params)


def top_long_short_account_ratio(self, symbol: str, period: str, **kwargs):
    """
    |
    | **Get top long short account ratio.**

    :API endpoint: ``GET /futures/data/topLongShortAccountRatio``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#top-trader-long-short-ratio-accounts

    :parameter symbol: string; the trading symbol.
    :parameter period: string; the period of open interest, "5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d". (see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info)
    :parameter limit: optional int; limit the results. Default 30, max 500.
    :parameter startTime: optional int
    :parameter endTime: optional int

    **Notes**
        - If startTime and endTime are not sent, the most recent data is returned.
        - Only the data of the latest 30 days is available.
    |
    """

    check_required_parameters([[symbol, "symbol"], [period, "period"]])
    params = {"symbol": symbol, "period": period, **kwargs}
    return self.query("/futures/data/topLongShortAccountRatio", params)


def taker_long_short_ratio(self, symbol: str, period: str, **kwargs):
    """
    |
    | **Get taker long short ratio.**

    :API endpoint: ``GET /futures/data/takerlongshortRatio``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#taker-buy-sell-volume

    :parameter symbol: string; the trading symbol.
    :parameter period: string; the period of open interest, "5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d". (see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info)
    :parameter limit: optional int; limit the results. Default 30, max 500.
    :parameter startTime: optional int
    :parameter endTime: optional int

    **Notes**
        - If startTime and endTime are not sent, the most recent data is returned.
        - Only the data of the latest 30 days is available.
    |
    """

    check_required_parameters([[symbol, "symbol"], [period, "period"]])
    params = {"symbol": symbol, "period": period, **kwargs}
    return self.query("/futures/data/takerlongshortRatio", params)


def blvt_kline(self, symbol: str, interval: str, **kwargs):
    """
    |
    | **Get Historical BLVT NAV Kline**

    :API endpoint: ``GET /fapi/v1/lvtKlines``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#historical-blvt-nav-kline-candlestick

    :parameter symbol: string; the trading symbol.
    :parameter period: string; the period of open interest, "5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d". (see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info)
    :parameter limit: optional int; limit the results. Default 500, max 1000.
    :parameter startTime: optional int
    :parameter endTime: optional int

    **Notes**
        - If startTime and endTime are not sent, the most recent data is returned.
    |
    """

    check_required_parameters([[symbol, "symbol"], [interval, "interval"]])
    params = {"symbol": symbol, "interval": interval, **kwargs}
    return self.query("/fapi/v1/lvtKlines", params)


def index_info(self, symbol: str = None):
    """
    |
    | **Get Index Composite**

    :API endpoint: ``GET /fapi/v1/indexInfo``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#composite-index-symbol-information

    :parameter symbol: optional string; the trading symbol.

    **Notes**
        - Only for composite index symbols.
    |
    """

    params = {
        "symbol": symbol,
    }
    return self.query("/fapi/v1/indexInfo", params)


def asset_Index(self, symbol: str = None):
    """
    |
    | **Get asset index for Multi-Assets mode**

    :API endpoint: ``GET /fapi/v1/assetIndex``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#multi-assets-mode-asset-index

    :parameter symbol: optional string; Asset pair in multi asset mode (ex: BTCUSD).
    |
    """

    params = {
        "symbol": symbol,
    }
    return self.query("/fapi/v1/assetIndex", params)
