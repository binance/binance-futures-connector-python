from typing import Optional

from binance.websocket.websocket_client import BinanceWebsocketClient


class CMFuturesWebsocketClient(BinanceWebsocketClient):
    def __init__(
        self,
        stream_url="wss://dstream.binance.com",
        on_message=None,
        on_open=None,
        on_close=None,
        on_error=None,
        on_ping=None,
        on_pong=None,
        on_disconnected=None,
        is_combined=False,
        proxies: Optional[dict] = None,
    ):
        if is_combined:
            stream_url = stream_url + "/stream"
        else:
            stream_url = stream_url + "/ws"
        super().__init__(
            stream_url,
            on_message=on_message,
            on_open=on_open,
            on_close=on_close,
            on_error=on_error,
            on_ping=on_ping,
            on_pong=on_pong,
            on_disconnected=on_disconnected,
            proxies=proxies,
        )

    def agg_trade(self, symbol: str, id=None, action=None, **kwargs):
        """Aggregate Trade Streams

        The Aggregate Trade Streams push market trade information that is aggregated for a single taker order every 100 milliseconds.
        Only market trades will be aggregated, which means the insurance fund trades and ADL trades won't be aggregated.

        Stream Name: <symbol>@aggTrade

        https://binance-docs.github.io/apidocs/delivery/en/#aggregate-trade-streams

        Update Speed: 100ms
        """
        stream_name = "{}@aggTrade".format(symbol.lower())

        self.send_message_to_server(stream_name, action=action, id=id)

    def index_price(self, pair: str, id=None, speed=1, action=None, **kwargs):
        """Index Price Streams

        Stream Name: <pair>@indexPrice OR <pair>@indexPrice@1s

        https://binance-docs.github.io/apidocs/delivery/en/#index-price-stream

        Update Speed: 3000ms OR 1000ms
        """
        if speed == 1:
            stream_name = "{}@indexPrice@{}s".format(pair.lower(), speed)
        else:
            stream_name = "{}@indexPrice".format(pair.lower())

        self.send_message_to_server(stream_name, action=action, id=id)

    def mark_price(self, symbol: str, speed=1, id=None, action=None, **kwargs):
        """Mark Price Streams

        Stream Name: <symbol>@markPrice OR <symbol>@markPrice@1s

        https://binance-docs.github.io/apidocs/delivery/en/#mark-price-stream

        Update Speed: 3000ms OR 1000ms
        """
        if speed == 1:
            stream_name = "{}@markPrice@{}s".format(symbol.lower(), speed)
        else:
            stream_name = "{}@markPrice".format(symbol.lower())

        self.send_message_to_server(stream_name, action=action, id=id)

    def pair_mark_price(self, pair: str, speed=1, id=None, action=None, **kwargs):
        """Mark Price of All Symbols of a Pair

        Stream Name: <pair>@markPrice OR <pair>@markPrice@1s

        https://binance-docs.github.io/apidocs/delivery/en/#mark-price-of-all-symbols-of-a-pair

        Update Speed: 3000ms OR 1000ms
        """
        if speed == 1:
            stream_name = "{}@markPrice@{}s".format(pair.lower(), speed)
        else:
            stream_name = "{}@markPrice".format(pair.lower())

        self.send_message_to_server(stream_name, action=action, id=id)

    def kline(self, symbol: str, interval: str, id=None, action=None, **kwargs):
        """Kline/Candlestick Streams

        The Kline/Candlestick Stream push updates to the current klines/candlestick every 250 milliseconds (if existing)

        Stream Name: <symbol>@kline_<interval>

        https://binance-docs.github.io/apidocs/delivery/en/#kline-candlestick-streams

        interval:
        m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

        - 1m
        - 3m
        - 5m
        - 15m
        - 30m
        - 1h
        - 2h
        - 4h
        - 6h
        - 8h
        - 12h
        - 1d
        - 3d
        - 1w
        - 1M

        Update Speed: 250ms
        """
        stream_name = "{}@kline_{}".format(symbol.lower(), interval)

        self.send_message_to_server(stream_name, action=action, id=id)

    def continuous_kline(
        self,
        pair: str,
        contractType: str,
        interval: str,
        id=None,
        action=None,
        **kwargs
    ):
        """Continuous Kline/Candlestick Streams

        The Kline/Candlestick Stream push updates to Kline/candlestick bars for a specific contract type. every 250 milliseconds

        Stream Name: <pair>_<contractType>@continuousKline_<interval>

        https://binance-docs.github.io/apidocs/delivery/en/#continuous-contract-kline-candlestick-streams

        interval:
        m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

        - 1m
        - 3m
        - 5m
        - 15m
        - 30m
        - 1h
        - 2h
        - 4h
        - 6h
        - 8h
        - 12h
        - 1d
        - 3d
        - 1w
        - 1M

        Update Speed: 250ms
        """
        stream_name = "{}_{}@continuousKline_{}".format(
            pair.lower(), contractType, interval
        )

        self.send_message_to_server(stream_name, action=action, id=id)

    def index_kline(self, pair: str, interval: str, id=None, action=None, **kwargs):
        """Kline/Candlestick chart intervals Streams

        Stream Name: <pair>@indexPriceKline_<interval>

        https://binance-docs.github.io/apidocs/delivery/en/#index-kline-candlestick-streams

        interval:
        m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

        - 1m
        - 3m
        - 5m
        - 15m
        - 30m
        - 1h
        - 2h
        - 4h
        - 6h
        - 8h
        - 12h
        - 1d
        - 3d
        - 1w
        - 1M

        Update Speed: 250ms
        """
        stream_name = "{}@indexPriceKline_{}".format(pair.lower(), interval)

        self.send_message_to_server(stream_name, action=action, id=id)

    def mark_kline(self, symbol: str, interval: str, id=None, action=None, **kwargs):
        """Kline/Candlestick chart intervals Streams

        Stream Name: <symbol>@markPriceKline_<interval>

        https://binance-docs.github.io/apidocs/delivery/en/#mark-price-kline-candlestick-streams

        interval:
        m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

        - 1m
        - 3m
        - 5m
        - 15m
        - 30m
        - 1h
        - 2h
        - 4h
        - 6h
        - 8h
        - 12h
        - 1d
        - 3d
        - 1w
        - 1M

        Update Speed: 250ms
        """
        stream_name = "{}@markPriceKline_{}".format(symbol.lower(), interval)

        self.send_message_to_server(stream_name, action=action, id=id)

    def mini_ticker(self, symbol=None, id=None, action=None, **kwargs):
        """Individual symbol or all symbols mini ticker

        24hr rolling window mini-ticker statistics.
        These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs

        Stream Name: <symbol>@miniTicker or
        Stream Name: !miniTicker@arr

        https://binance-docs.github.io/apidocs/delivery/en/#individual-symbol-mini-ticker-stream
        https://binance-docs.github.io/apidocs/delivery/en/#all-market-mini-tickers-stream

        Update Speed: 500ms for individual symbol, 1000ms for all market symbols
        """

        if symbol is None:
            stream_name = "!miniTicker@arr"
        else:
            stream_name = "{}@miniTicker".format(symbol.lower())

        self.send_message_to_server(stream_name, action=action, id=id)

    def ticker(self, symbol=None, id=None, action=None, **kwargs):
        """Individual symbol or all symbols ticker

        24hr rolling window ticker statistics for a single symbol.
        These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before.

        Stream Name: <symbol>@ticker or
        Stream Name: !ticker@arr

        https://binance-docs.github.io/apidocs/delivery/en/#individual-symbol-ticker-streams
        https://binance-docs.github.io/apidocs/delivery/en/#all-market-tickers-streams

        Update Speed: 500ms for individual symbol, 1000ms for all market symbols
        """

        if symbol is None:
            stream_name = "!ticker@arr"
        else:
            stream_name = "{}@ticker".format(symbol.lower())
        self.send_message_to_server(stream_name, action=action, id=id)

    def book_ticker(self, symbol, id=None, action=None, **kwargs):
        """Individual symbol or all book ticker

        Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol.

        Stream Name: <symbol>@bookTicker or
        Stream Name: !bookTicker

        https://binance-docs.github.io/apidocs/delivery/en/#individual-symbol-book-ticker-streams
        https://binance-docs.github.io/apidocs/delivery/en/#all-book-tickers-stream

        Update Speed: Real-time
        """
        if symbol is None:
            stream_name = "!bookTicker"
        else:
            stream_name = "{}@bookTicker".format(symbol.lower())
        self.send_message_to_server(stream_name, action=action, id=id)

    def diff_book_depth(self, symbol: str, speed=100, id=None, action=None, **kwargs):
        """Diff. Depth Stream
        Order book price and quantity depth updates used to locally manage an order book.

        Stream Name: <symbol>@depth OR <symbol>@depth@500ms OR<symbol>@depth@100ms

        https://binance-docs.github.io/apidocs/delivery/en/#diff-book-depth-streams

        Update Speed: 250ms, 500ms or 100ms
        """

        self.send_message_to_server(
            "{}@depth@{}ms".format(symbol.lower(), speed), action=action, id=id
        )

    def partial_book_depth(
        self, symbol: str, level=5, speed=500, id=None, action=None, **kwargs
    ):
        """Partial Book Depth Streams

        Top bids and asks, Valid are 5, 10, or 20.

        Stream Names: <symbol>@depth<levels> OR <symbol>@depth<levels>@500ms OR <symbol>@depth<levels>@100ms

        https://binance-docs.github.io/apidocs/delivery/en/#partial-book-depth-streams

        Update Speed: 250ms, 500ms or 100ms
        """
        self.send_message_to_server(
            "{}@depth{}@{}ms".format(symbol.lower(), level, speed), id=id, action=action
        )

    def liquidation_order(self, symbol: str, id=None, action=None, **kwargs):
        """The Liquidation Order Snapshot Streams push force liquidation order information for specific symbol.
        The All Liquidation Order Snapshot Streams push force liquidation order information for all symbols in the market.

        For each symbol，only the latest one liquidation order within 1000ms will be pushed as the snapshot. If no liquidation happens in the interval of 1000ms, no stream will be pushed.

        Stream Name: <symbol>@forceOrder or !forceOrder@arr

        https://binance-docs.github.io/apidocs/delivery/en/#liquidation-order-streams
        https://binance-docs.github.io/apidocs/delivery/en/#all-market-liquidation-order-streams

        Update Speed: 1000ms
        """
        if symbol is None:
            stream_name = "!forceOrder@arr"
        else:
            stream_name = "{}@forceOrder".format(symbol.lower())
        self.send_message_to_server(stream_name, id=id, action=action)

    def user_data(self, listen_key: str, id=None, action=None, **kwargs):
        """Listen to user data by using the provided listen_key"""
        self.send_message_to_server(listen_key, action=action, id=id)
