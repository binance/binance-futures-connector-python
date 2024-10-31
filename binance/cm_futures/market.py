from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters


def ping(self):
    """
    |
    | **Test Connectivity**
    | *Test connectivity to the Rest API.*

    :API endpoint: ``GET /dapi/v1/ping``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Test-Connectivity
    |
    """

    url_path = "/dapi/v1/ping"
    return self.query(url_path)


def time(self):
    """
    |
    | **Check Server Time**
    | *Test connectivity to the Rest API and get the current server time.*

    :API endpoint: ``GET /dapi/v1/time``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Check-Server-time
    |
    """

    url_path = "/dapi/v1/time"
    return self.query(url_path)


def exchange_info(self):
    """
    |
    | **Exchange Information**
    | *Current exchange trading rules and symbol information*

    :API endpoint: ``GET /dapi/v1/exchangeInfo``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Exchange-Information
    |
    """

    url_path = "/dapi/v1/exchangeInfo"
    return self.query(url_path)


def depth(self, symbol: str, **kwargs):
    """
    |
    | **Get Orderbook**

    :API endpoint: ``GET /dapi/v1/depth``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Order-Book

    :parameter symbol: string; the trading pair
    :parameter limit: optional int; limit the results. Default 500, valid limits: [5, 10, 20, 50, 100, 500, 1000].
    |
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.query("/dapi/v1/depth", params)


def trades(self, symbol: str, **kwargs):
    """
    |
    | **Get Recent Market Trades**

    :API endpoint: ``GET /dapi/v1/trades``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Recent-Trades-List

    :parameter symbol: string; the trading pair
    :parameter limit: optional int; limit the results. Default 500, max 1000.
    |
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.query("/dapi/v1/trades", params)


def historical_trades(self, symbol: str, **kwargs):
    """
    |
    | **Old Trade Lookup**
    | *Get older market historical trades.*

    :API endpoint: ``GET /dapi/v1/historicalTrades``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Old-Trades-Lookup

    :parameter symbol: string; the trading pair
    :parameter limit: optional int; limit the results. Default 500, max 1000.
    :parameter formId: optional int; trade ID to fetch from. Default gets most recent trades.
    |
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.limit_request("GET", "/dapi/v1/historicalTrades", params)


def agg_trades(self, symbol: str, **kwargs):
    """
    |
    | **Compressed/Aggregate Trades List**
    | *Get compressed, aggregate market trades. Market trades that fill at the time, from the same order, with the same price will have the quantity aggregated.*

    :API endpoint: ``GET /dapi/v1/aggTrades``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Compressed-Aggregate-Trades-List

    :parameter symbol: string; the trading pair
    :parameter limit: optional int; limit the results. Default 500, max 1000.
    :parameter formId: optional int; trade ID to fetch from. Default gets most recent trades.
    :parameter startTime: optional int; Timestamp in ms to get aggregate trades from INCLUSIVE.
    :parameter endTime: optional int; Timestamp in ms to get aggregate trades until INCLUSIVE.
    |
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.query("/dapi/v1/aggTrades", params)


def klines(self, symbol: str, interval: str, **kwargs):
    """
    |
    | **Kline/Candlestick Data**
    | *Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.*

    :API endpoint: ``GET /dapi/v1/klines``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Kline-Candlestick-Data

    :parameter symbol: string; the trading pair
    :parameter interval: string; the interval of kline, e.g 1m, 5m, 1h, 1d, etc. (see more in https://developers.binance.com/docs/derivatives/coin-margined-futures/common-definition)
    :parameter limit: optional int; limit the results. Default 500, max 1000.
    :parameter startTime: optional int; Timestamp in ms to get aggregate trades from INCLUSIVE.
    :parameter endTime: optional int; Timestamp in ms to get aggregate trades until INCLUSIVE.
    |
    """

    check_required_parameters([[symbol, "symbol"], [interval, "interval"]])
    params = {"symbol": symbol, "interval": interval, **kwargs}
    return self.query("/dapi/v1/klines", params)


def continuous_klines(self, pair: str, contractType: str, interval: str, **kwargs):
    """
    |
    | **Continuous Kline/Candlestick Data**
    | *Kline/candlestick bars for a specific contract type. Klines are uniquely identified by their open time.*

    :API endpoint: ``GET /dapi/v1/continuousKlines``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Continuous-Contract-Kline-Candlestick-Data

    :parameter pair: string; the trading pair
    :parameter contractType: string; PERPETUAL, CURRENT_MONTH, NEXT_MONTH, CURRENT_QUARTER, NEXT_QUARTER.
    :parameter interval: string; the interval of kline, e.g 1m, 5m, 1h, 1d, etc. (see more in https://developers.binance.com/docs/derivatives/coin-margined-futures/common-definition)
    :parameter limit: optional int; limit the results. Default 500, max 1000.
    :parameter startTime: optional int; Timestamp in ms to get aggregate trades from INCLUSIVE.
    :parameter endTime: optional int; Timestamp in ms to get aggregate trades until INCLUSIVE.
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
    return self.query("/dapi/v1/continuousKlines", params)


def index_price_klines(self, pair: str, interval: str, **kwargs):
    """
    |
    | **Kline/Candlestick Data for the index price of a pair.**
    | *Klines are uniquely identified by their open time.*

    :API endpoint: ``GET /dapi/v1/indexPriceKlines``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Index-Price-Kline-Candlestick-Data

    :parameter pair: string; the trading pair
    :parameter interval: string; the interval of kline, e.g 1m, 5m, 1h, 1d, etc. (see more in https://developers.binance.com/docs/derivatives/coin-margined-futures/common-definition)
    :parameter limit: optional int; limit the results. Default 500, max 1000.
    :parameter startTime: optional int; Timestamp in ms to get aggregate trades from INCLUSIVE.
    :parameter endTime: optional int; Timestamp in ms to get aggregate trades until INCLUSIVE.
    |
    """

    check_required_parameters([[pair, "pair"], [interval, "interval"]])
    params = {"pair": pair, "interval": interval, **kwargs}
    return self.query("/dapi/v1/indexPriceKlines", params)


def mark_price_klines(self, symbol: str, interval: str, **kwargs):
    """
    |
    | **Kline/candlestick bars for the mark price of a symbol.**
    | *Klines are uniquely identified by their open time.*

    :API endpoint: ``GET /dapi/v1/markPriceKlines``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Mark-Price-Kline-Candlestick-Data

    :parameter pair: string; the trading pair
    :parameter interval: string; the interval of kline, e.g 1m, 5m, 1h, 1d, etc. (see more in https://developers.binance.com/docs/derivatives/coin-margined-futures/common-definition)
    :parameter limit: optional int; limit the results. Default 500, max 1000.
    :parameter startTime: optional int; Timestamp in ms to get aggregate trades from INCLUSIVE.
    :parameter endTime: optional int; Timestamp in ms to get aggregate trades until INCLUSIVE.

    **Notes**
        - The difference between startTime and endTime can only be up to 200 days
        - Between startTime and endTime, the most recent limit data from endTime will be returned:
        - If startTime and endTime are not sent, current timestamp will be set as endTime, and the most recent data will be returned.
        - If startTime is sent only, the timestamp of 200 days after startTime will be set as endTime(up to the current time)
        - If endTime is sent only, the timestamp of 200 days before endTime will be set as startTime
    |
    """

    check_required_parameters([[symbol, "symbol"], [interval, "interval"]])
    params = {"symbol": symbol, "interval": interval, **kwargs}
    return self.query("/dapi/v1/markPriceKlines", params)


def mark_price(self, symbol: str):
    """
    |
    | **Mark Price and Funding Rate**

    :API endpoint: ``GET /dapi/v1/premiumIndex``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Index-Price-and-Mark-Price

    :parameter symbol: string; the trading pair
    |
    """

    check_required_parameter(symbol, "symbol")
    params = {
        "symbol": symbol,
    }
    return self.query("/dapi/v1/premiumIndex", params)


def funding_rate(self, symbol: str, **kwargs):
    """
    |
    | **Funding Rate History**

    :API endpoint: ``GET /dapi/v1/fundingRate``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Get-Funding-Rate-History-of-Perpetual-Futures

    :parameter symbol: string; the trading pair
    :parameter limit: optional int; limit the results. Default 500, max 1000.
    :parameter startTime: optional int; Timestamp in ms to get aggregate trades from INCLUSIVE.
    :parameter endTime: optional int; Timestamp in ms to get aggregate trades until INCLUSIVE.

    **Notes**
        - Empty array will be returned for delivery symbols.
    |
    """

    params = {"symbol": symbol, **kwargs}
    return self.query("/dapi/v1/fundingRate", params)


def ticker_24hr_price_change(self, symbol: str = None, pair: str = None):
    """
    |
    | **24 hour rolling window price change statistics.**
    | *Careful when accessing this with no symbol.*
    | *If the symbol is not sent, tickers for all symbols will be returned in an array.*

    :API endpoint: ``GET /dapi/v1/ticker/24hr``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/24hr-Ticker-Price-Change-Statistics

    :parameter symbol: optional string; the trading symbol
    :parameter pair: optional string; the trading pair

    **Notes**
        - Symbol and pair cannot be sent together
        - If a pair is sent, tickers for all symbols of the pair will be returned
        - If either a pair or symbol is sent, tickers for all symbols of all pairs will be returned
    |
    """

    if (symbol is None) and (pair is None):
        return self.query("/dapi/v1/ticker/24hr")
    elif symbol is None:
        params = {"pair": pair}
    else:
        params = {"symbol": symbol}

    return self.query("/dapi/v1/ticker/24hr", params)


def ticker_price(self, symbol: str = None, pair: str = None):
    """
    |
    | **Latest price for a symbol or symbols**

    :API endpoint: ``GET /dapi/v1/ticker/price``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Symbol-Price-Ticker

    :parameter symbol: optional string; the trading symbol
    :parameter pair: optional string; the trading pair

    **Notes**
        - Symbol and pair cannot be sent together
        - If a pair is sent,tickers for all symbols of the pair will be returned
        - If either a pair or symbol is sent, tickers for all symbols of all pairs will be returned
    |
    """

    if (symbol is None) and (pair is None):
        return self.query("/dapi/v1/ticker/price")
    elif symbol is None:
        params = {"pair": pair}
    else:
        params = {"symbol": symbol}

    return self.query("/dapi/v1/ticker/price", params)


def book_ticker(self, symbol: str = None, pair: str = None):
    """
    |
    | **Best price/qty on the order book for a symbol or symbols**

    :API endpoint: ``GET /dapi/v1/ticker/bookTicker``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Symbol-Order-Book-Ticker

    :parameter symbol: optional string; the trading symbol

    **Notes**
        - If the symbol is not sent, bookTickers for all symbols will be returned in an array.
    |
    """

    if (symbol is None) and (pair is None):
        return self.query("/dapi/v1/ticker/bookTicker")
    elif symbol is None:
        params = {"pair": pair}
    else:
        params = {"symbol": symbol}

    return self.query("/dapi/v1/ticker/bookTicker", params)


def query_index_price_constituents(self, symbol: str):
    """
    |
    | **Query Index Price Constituents**

    :API endpoint: ``GET /dapi/v1/constituents``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Index-Constituents

    :parameter symbol: string; symbol underlying e.g BTCUSD
    |
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol}
    return self.query("/dapi/v1/constituents", params)


def open_interest(self, symbol: str):
    """
    |
    | **Get present open interest of a specific symbol**

    :API endpoint: ``GET /dapi/v1/openInterest``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Open-Interest

    :parameter symbol: string; the trading symbol
    |
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol}
    return self.query("/dapi/v1/openInterest", params)


def open_interest_hist(self, pair: str, contractType: str, period: str, **kwargs):
    """
    |
    | **Get historical open interest of a specific symbol**

    :API endpoint: ``GET /futures/data/openInterestHist``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Open-Interest-Statistics

    :parameter pair: string; the trading pair
    :parameter contractType: string; ALL, CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL.
    :parameter period: string; the period of open interest, "5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d". (see more in https://developers.binance.com/docs/derivatives/coin-margined-futures/common-definition)
    :parameter limit: optional int; limit the results. Default 30, max 500.
    :parameter startTime: optional int
    :parameter endTime: optional int

    **Notes**
        - If startTime and endTime are not sent, the most recent data is returned.
        - Only the data of the latest 30 days is available.
    |
    """

    check_required_parameters(
        [[pair, "pair"], [contractType, "contractType"], [period, "period"]]
    )
    params = {"pair": pair, "contractType": contractType, "period": period, **kwargs}
    return self.query("/futures/data/openInterestHist", params)


def top_long_short_account_ratio(self, pair: str, period: str, **kwargs):
    """
    |
    | **Get top long short account ratio**

    :API endpoint: `GET /futures/data/topLongShortAccountRatio`
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Top-Long-Short-Account-Ratio

    :parameter pair: string; the trading pair
    :parameter period: string; the period of open interest, "5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d". (see more in https://developers.binance.com/docs/derivatives/coin-margined-futures/common-definition)
    :parameter limit: optional int; limit the results. Default 30, max 500.
    :parameter startTime: optional int
    :parameter endTime: optional int

    **Notes**
        - If startTime and endTime are not sent, the most recent data is returned.
        - Only the data of the latest 30 days is available.
    |
    """

    check_required_parameters([[pair, "pair"], [period, "period"]])
    params = {"pair": pair, "period": period, **kwargs}
    return self.query("/futures/data/topLongShortAccountRatio", params)


def top_long_short_position_ratio(self, pair: str, period: str, **kwargs):
    """
    |
    | **Get top long short position ratio**

    :API endpoint: ``GET /futures/data/topLongShortPositionRatio``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Top-Trader-Long-Short-Ratio

    :parameter pair: string; the trading pair
    :parameter period: string; the period of open interest, "5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d". (see more in https://developers.binance.com/docs/derivatives/coin-margined-futures/common-definition)
    :parameter limit: optional int; limit the results. Default 30, max 500.
    :parameter startTime: optional int
    :parameter endTime: optional int

    **Notes**
        - If startTime and endTime are not sent, the most recent data is returned.
        - Only the data of the latest 30 days is available.
    |
    """

    check_required_parameters([[pair, "pair"], [period, "period"]])
    params = {"pair": pair, "period": period, **kwargs}
    return self.query("/futures/data/topLongShortPositionRatio", params)


def long_short_account_ratio(self, pair: str, period: str, **kwargs):
    """
    |
    | **Get top long short account ratio**

    :API endpoint: ``GET /futures/data/globalLongShortAccountRatio``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Long-Short-Ratio

    :parameter pair: string; the trading pair
    :parameter period: string; the period of open interest, "5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d". (see more in https://developers.binance.com/docs/derivatives/coin-margined-futures/common-definition)
    :parameter limit: optional int; limit the results. Default 30, max 500.
    :parameter startTime: optional int
    :parameter endTime: optional int

    **Notes**
        - If startTime and endTime are not sent, the most recent data is returned.
        - Only the data of the latest 30 days is available.
    |
    """

    check_required_parameters([[pair, "pair"], [period, "period"]])
    params = {"pair": pair, "period": period, **kwargs}
    return self.query("/futures/data/globalLongShortAccountRatio", params)


def taker_long_short_ratio(self, pair: str, contractType: str, period: str, **kwargs):
    """
    |
    | **Get taker long short ratio**

    :API endpoint: ``GET /futures/data/takerBuySellVol``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Taker-Buy-Sell-Volume

    :parameter pair: string; the trading pair
    :parameter contractType: string; CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL.
    :parameter period: string; the period of open interest, "5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d". (see more in https://developers.binance.com/docs/derivatives/coin-margined-futures/common-definition)
    :parameter limit: optional int; limit the results. Default 30, max 500.
    :parameter startTime: optional int
    :parameter endTime: optional int

    **Notes**
        - If startTime and endTime are not sent, the most recent data is returned.
        - Only the data of the latest 30 days is available.
    |
    """

    check_required_parameters(
        [[pair, "pair"], [contractType, "contractType"], [period, "period"]]
    )
    params = {"pair": pair, "contractType": contractType, "period": period, **kwargs}
    return self.query("/futures/data/takerBuySellVol", params)


def basis(self, pair: str, contractType: str, period: str, **kwargs):
    """
    |
    | **Get Index Composite**

    :API endpoint: ``GET /futures/data/basis``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/Basis

    :parameter pair: string; the trading pair
    :parameter contractType: string; CURRENT_QUARTER, NEXT_QUARTER, PERPETUAL.
    :parameter period: string; the period of open interest, "5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1d". (see more in https://developers.binance.com/docs/derivatives/coin-margined-futures/common-definition)
    :parameter limit: optional int; limit the results. Default 30, max 500.
    :parameter startTime: optional int
    :parameter endTime: optional int

    **Notes**
        - If startTime and endTime are not sent, the most recent data is returned.
        - Only the data of the latest 30 days is available.
    |
    """

    check_required_parameters(
        [[pair, "pair"], [contractType, "contractType"], [period, "period"]]
    )
    params = {"pair": pair, "contractType": contractType, "period": period, **kwargs}
    return self.query("/futures/data/basis", params)
