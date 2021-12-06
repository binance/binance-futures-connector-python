from binance.lib.utils import (
    check_required_parameter,
)
from binance.lib.utils import check_required_parameters


def ping(self):
    """Test Connectivity
    Test connectivity to the Rest API.

    GET /fapi/v1/ping

    https://binance-docs.github.io/apidocs/futures/en/#test-connectivity

    """

    url_path = "/fapi/v1/ping"
    return self.query(url_path)


def time(self):
    """Check Server Time
    Test connectivity to the Rest API and get the current server time.

    GET /fapi/v1/time

    https://binance-docs.github.io/apidocs/futures/en/#check-server-time

    """

    url_path = "/fapi/v1/time"
    return self.query(url_path)


def exchange_info(self):
    """Exchange Information
    Current exchange trading rules and symbol information

    GET /fapi/v1/exchangeInfo

    https://binance-docs.github.io/apidocs/futures/en/#exchange-information

    """

    url_path = "/fapi/v1/exchangeInfo"
    return self.query(url_path)


def depth(self, symbol: str, **kwargs):
    """Get orderbook

    GET /fapi/v1/depth

    https://binance-docs.github.io/apidocs/futures/en/#order-book

    Args:
        symbol (str): the trading symbol
    Keyword Args:
        limit (int, optional): limit the results. Default 500; valid limits:[5, 10, 20, 50, 100, 500, 1000]
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.query("/fapi/v1/depth", params)


def trades(self, symbol: str, **kwargs):
    """Get recent market trades

    GET /fapi/v1/trades

    https://binance-docs.github.io/apidocs/futures/en/#recent-trades-list

    Args:
        symbol (str): the trading symbol
    Keyword Args:
        limit (int, optional): limit the results. Default 500; max 1000
    """
    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.query("/fapi/v1/trades", params)


def historical_trades(self, symbol: str, **kwargs):
    """Old Trade Lookup
    Get older market historical trades.

    GET /fapi/v1/historicalTrades

    https://binance-docs.github.io/apidocs/futures/en/#old-trades-lookup-market_data

    Args:
        symbol (str): the trading symbol
    Keyword Args:
        limit (int, optional): limit the results. Default 500; max 1000.
        formId (int, optional): trade id to fetch from. Default gets most recent trades.
    """
    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.limit_request("GET", "/fapi/v1/historicalTrades", params)


def agg_trades(self, symbol: str, **kwargs):
    """Compressed/Aggregate Trades List
    Get compressed, aggregate market trades. Market trades that fill at the time, from the same order, with the same price will have the quantity aggregated.
    
    GET /fapi/v1/aggTrades

    https://binance-docs.github.io/apidocs/futures/en/#compressed-aggregate-trades-list

    Args:
        symbol (str): the trading symbol
    Keyword Args:
        limit (int, optional): limit the results. Default 500; max 1000.
        formId (int, optional): id to get aggregate trades from INCLUSIVE.
        startTime (int, optional): Timestamp in ms to get aggregate trades from INCLUSIVE.
        endTime (int, optional): Timestamp in ms to get aggregate trades until INCLUSIVE.
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.query("/fapi/v1/aggTrades", params)


def klines(self, symbol: str, interval: str, **kwargs):
    """Kline/Candlestick Data
    Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.

    GET /fapi/v1/klines

    https://binance-docs.github.io/apidocs/futures/en/#kline-candlestick-data

    Args:
        symbol (str): the trading symbol
        interval (str): the interval of kline, e.g 1m, 5m, 1h, 1d, etc.
        (see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info)
    Keyword Args:
        limit (int, optional): limit the results. Default 500; max 1000.
        startTime (int, optional): Start Time.
        endTime (int, optional): End Time.
    """
    check_required_parameters([[symbol, "symbol"], [interval, "interval"]])

    params = {"symbol": symbol, "interval": interval, **kwargs}
    return self.query("/fapi/v1/klines", params)


def continuous_klines(self, pair: str, contractType: str, interval: str, **kwargs):
    """Continuous Kline/Candlestick Data
    Kline/candlestick bars for a specific contract type. Klines are uniquely identified by their open time.  
    
    GET /fapi/v1/continuousKlines

    https://binance-docs.github.io/apidocs/futures/en/#continuous-contract-kline-candlestick-data

    Args:
        pair (str): the trading pair
        contractType: PERPETUAL, CURRENT_MONTH, NEXT_MONTH, CURRENT_QUARTER, NEXT_QUARTER 
        interval (str): the interval of kline, e.g 1m, 5m, 1h, 1d, etc.
        (see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info)
    Keyword Args:
        limit (int, optional): limit the results. Default 500; max 1000.
        startTime (int, optional): Start Time.
        endTime (int, optional): End Time.
    """
    check_required_parameters([[pair, "pair"], [contractType,"contractType"], [interval, "interval"]])

    params = {"pair": pair, "contractType":contractType, "interval": interval, **kwargs}
    return self.query("/fapi/v1/continuousKlines", params)


def index_price_klines(self, pair: str, interval: str, **kwargs):
    """Kline/Candlestick Data for the index price of a pair.
    Klines are uniquely identified by their open time.    
    
    GET /fapi/v1/indexPriceKlines

    https://binance-docs.github.io/apidocs/futures/en/#index-price-kline-candlestick-data

    Args:
        pair (str): the trading pair
        interval (str): the interval of kline, e.g 1m, 5m, 1h, 1d, etc.
        (see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info)
    Keyword Args:
        limit (int, optional): limit the results. Default 500; max 1000.
        startTime (int, optional): Start Time.
        endTime (int, optional): End Time.
    """
    check_required_parameters([[pair, "pair"], [interval, "interval"]])

    params = {"pair": pair, "interval": interval, **kwargs}
    return self.query("/fapi/v1/indexPriceKlines", params)


def mark_price_klines(self, symbol: str, interval: str, **kwargs):
    """Kline/candlestick bars for the mark price of a symbol.
    Klines are uniquely identified by their open time.   
    
    GET /fapi/v1/markPriceKlines

    https://binance-docs.github.io/apidocs/futures/en/#mark-price-kline-candlestick-data

    Args:
        symbol (str): the trading symbol
        interval (str): the interval of kline, e.g 1m, 5m, 1h, 1d, etc.
        (see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info)
    Keyword Args:
        limit (int, optional): limit the results. Default 500; max 1000.
        startTime (int, optional): Start Time.
        endTime (int, optional): End Time.
    """
    check_required_parameters([[symbol, "symbol"], [interval, "interval"]])

    params = {"symbol": symbol, "interval": interval, **kwargs}
    return self.query("/fapi/v1/markPriceKlines", params)


def mark_price(self, symbol: str):
    """Mark Price and Funding Rate

    GET /fapi/v1/premiumIndex

    https://binance-docs.github.io/apidocs/futures/en/#mark-price

    Args:
        symbol (str): the trading symbol
    """

    check_required_parameter(symbol, "symbol")
    params = {
        "symbol": symbol,
    }
    return self.query("/fapi/v1/premiumIndex", params)


def funding_rate(self, symbol: str,  **kwargs):
    """funding Rate history

    GET /fapi/v1/fundingRate

    https://binance-docs.github.io/apidocs/futures/en/#get-funding-rate-history

    Args:
        symbol (str, optional): the trading symbol
    Keyword Args:
        limit (int, optional): limit the results. Default 100; max 1000.
        startTime (int, optional): Start Time.
        endTime (int, optional): End Time.

    If startTime and endTime are not sent, the most recent limit datas are returned.
    If the number of data between startTime and endTime is larger than limit, return as startTime + limit.
    In ascending order.
    """
    
    params = {"symbol": symbol, **kwargs}
    return self.query("/fapi/v1/fundingRate", params)


def ticker_24hr_price_change(self, symbol: str = None):
    """24 hour rolling window price change statistics. Careful when accessing this with no symbol.
    If the symbol is not sent, tickers for all symbols will be returned in an array.

    GET /fapi/v1/ticker/24hr

    https://binance-docs.github.io/apidocs/futures/en/#24hr-ticker-price-change-statistics

    Args:
        symbol (str, optional): the trading symbol
    """

    params = {
        "symbol": symbol,
    }
    return self.query("/fapi/v1/ticker/24hr", params)


def ticker_price(self, symbol: str = None):
    """Latest price for a symbol or symbols.

    GET /fapi/v1/ticker/price

    https://binance-docs.github.io/apidocs/futures/en/#symbol-price-ticker

    Args:
        symbol (str, optional): the trading symbol
    If the symbol is not sent, prices for all symbols will be returned in an array.
    """

    params = {
        "symbol": symbol,
    }
    return self.query("/fapi/v1/ticker/price", params)


def book_ticker(self, symbol: str = None):
    """Best price/qty on the order book for a symbol or symbols.

    GET /fapi/v1/ticker/bookTicker

    https://binance-docs.github.io/apidocs/futures/en/#symbol-order-book-ticker

    Args:
        symbol (str, optional): the trading symbol
    If the symbol is not sent, bookTickers for all symbols will be returned in an array.
    """

    params = {
        "symbol": symbol,
    }
    return self.query("/fapi/v1/ticker/bookTicker", params)


def open_interest(self, symbol: str):
    """Get present open interest of a specific symbol.

    GET /fapi/v1/openInterest

    https://binance-docs.github.io/apidocs/futures/en/#open-interest

    Args:
        symbol (str): the trading symbol
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol}
    return self.query("/fapi/v1/ticker/bookTicker", params)


def open_interest_hist(self, symbol: str, period: str, **kwargs):
    """Get historical open interest of a specific symbol.
    
    GET /futures/data/openInterestHist

    https://binance-docs.github.io/apidocs/futures/en/#open-interest-statistics

    Args:
        symbol (str): the trading symbol
        period (str): the period of open interest, "5m","15m","30m","1h","2h","4h","6h","12h","1d".
    Keyword Args:
        limit (int, optional): limit the results. Default 30; max 500.
        startTime (int, optional): Start Time.
        endTime (int, optional): End Time.
    If startTime and endTime are not sent, the most recent data is returned.
    Only the data of the latest 30 days is available.
    """
    check_required_parameters([[symbol, "symbol"], [period, "period"]])

    params = {"symbol": symbol, "period": period, **kwargs}
    return self.query("/futures/data/openInterestHist", params)


def top_long_short_position_ratio(self, symbol: str, period: str, **kwargs):
    """Get top long short position ratio.
    
    GET /futures/data/topLongShortPositionRatio

    https://binance-docs.github.io/apidocs/futures/en/#top-trader-long-short-ratio-positions

    Args:
        symbol (str): the trading symbol
        period (str): "5m","15m","30m","1h","2h","4h","6h","12h","1d".
        (see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info)
    Keyword Args:
        limit (int, optional): limit the results. Default 30; max 500.
        startTime (int, optional): Start Time.
        endTime (int, optional): End Time.
    If startTime and endTime are not sent, the most recent data is returned.
    Only the data of the latest 30 days is available.
    """
    check_required_parameters([[symbol, "symbol"], [period, "period"]])

    params = {"symbol": symbol, "period": period, **kwargs}
    return self.query("/futures/data/topLongShortPositionRatio", params)


def long_short_account_ratio(self, symbol: str, period: str, **kwargs):
    """Get top long short account ratio.
    
    GET /futures/data/globalLongShortAccountRatio

    https://binance-docs.github.io/apidocs/futures/en/#long-short-ratio

    Args:
        symbol (str): the trading symbol
        period (str): "5m","15m","30m","1h","2h","4h","6h","12h","1d".
    Keyword Args:
        limit (int, optional): limit the results. Default 30; max 500.
        startTime (int, optional)
        endTime (int, optional)
    If startTime and endTime are not sent, the most recent data is returned.
    Only the data of the latest 30 days is available.
    """
    check_required_parameters([[symbol, "symbol"], [period, "period"]])

    params = {"symbol": symbol, "period": period, **kwargs}
    return self.query("/futures/data/globalLongShortAccountRatio", params)


def taker_long_short_ratio(self, symbol: str, period: str, **kwargs):
    """Get taker long short ratio.
    
    GET /futures/data/takerlongshortRatio

    https://binance-docs.github.io/apidocs/futures/en/#taker-buy-sell-volume

    Args:
        symbol (str): the trading symbol
        period (str): "5m","15m","30m","1h","2h","4h","6h","12h","1d".
    Keyword Args:
        limit (int, optional): limit the results. Default 30; max 500.
        startTime (int, optional)
        endTime (int, optional)
    If startTime and endTime are not sent, the most recent data is returned.
    Only the data of the latest 30 days is available.
    """
    check_required_parameters([[symbol, "symbol"], [period, "period"]])

    params = {"symbol": symbol, "period": period, **kwargs}
    return self.query("/futures/data/takerlongshortRatio", params)


def blvt_kline(self, symbol: str, interval: str, **kwargs):
    """Get Historical BLVT NAV Kline
    
    GET /fapi/v1/lvtKlines

    https://binance-docs.github.io/apidocs/futures/en/#historical-blvt-nav-kline-candlestick

    Args:
        symbol (str): the trading symbol
        interval (str)
        (see more in https://binance-docs.github.io/apidocs/futures/en/#public-endpoints-info)
    Keyword Args:
        limit (int, optional): limit the results. Default 500; max 1000.
        startTime (int, optional)
        endTime (int, optional)
    If startTime and endTime are not sent, the most recent data is returned.
    """
    check_required_parameters([[symbol, "symbol"], [interval, "interval"]])

    params = {"symbol": symbol, "interval": interval, **kwargs}
    return self.query("/fapi/v1/lvtKlines", params)


def index_info(self, symbol: str = None):
    """Get index composite

    GET /fapi/v1/indexInfo

    https://binance-docs.github.io/apidocs/futures/en/#composite-index-symbol-information

    Args:
        symbol (str, optional): the trading symbol
    Only for composite index symbols
    """

    params = {
        "symbol": symbol,
    }
    return self.query("/fapi/v1/indexInfo", params)


def asset_Index(self, symbol: str = None):
    """Get asset index for Multi-Assets mode

    GET /fapi/v1/assetIndex

    https://binance-docs.github.io/apidocs/futures/en/#multi-assets-mode-asset-index

    Args:
        symbol (str, optional): Asset pair in multi asset mode(like BTCUSD)
    """

    params = {
        "symbol": symbol,
    }
    return self.query("/fapi/v1/assetIndex", params)
