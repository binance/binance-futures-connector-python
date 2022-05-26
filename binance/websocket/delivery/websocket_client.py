from binance.websocket.websocket_client import BinanceWebsocketClient


class DeliveryWebsocketClient(BinanceWebsocketClient):
    def __init__(self, stream_url="wss://dstream.binance.com"):
        super().__init__(stream_url)

    def agg_trade(self, symbol: str, id: int, callback, **kwargs):
        """Aggregate Trade Streams

        The Aggregate Trade Streams push market trade information that is aggregated for a single taker order every 100 milliseconds.
        Only market trades will be aggregated, which means the insurance fund trades and ADL trades won't be aggregated.

        Stream Name: <symbol>@aggTrade

        https://binance-docs.github.io/apidocs/delivery/en/#aggregate-trade-streams

        Update Speed: 100ms
        """
        self.live_subscribe(
            "{}@aggTrade".format(symbol.lower()), id, callback, **kwargs
        )

    def index_price(self, pair: str, id: int, speed: int, callback, **kwargs):
        """Index Price Streams

        Stream Name: <pair>@indexPrice OR <pair>@indexPrice@1s

        https://binance-docs.github.io/apidocs/delivery/en/#index-price-stream

        Update Speed: 3000ms OR 1000ms
        """
        self.live_subscribe(
            "{}@indexPrice@{}s".format(pair.lower(), speed), id, callback, **kwargs
        )

    def mark_price(self, symbol: str, id: int, speed: int, callback, **kwargs):
        """Mark Price Streams

        Stream Name: <symbol>@markPrice OR <symbol>@markPrice@1s

        https://binance-docs.github.io/apidocs/delivery/en/#mark-price-stream

        Update Speed: 3000ms OR 1000ms
        """
        self.live_subscribe(
            "{}@markPrice@{}s".format(symbol.lower(), speed), id, callback, **kwargs
        )

    def pair_mark_price(self, pair: str, id: int, speed: int, callback, **kwargs):
        """Mark Price of All Symbols of a Pair

        Stream Name: <pair>@markPrice OR <pair>@markPrice@1s

        https://binance-docs.github.io/apidocs/delivery/en/#mark-price-of-all-symbols-of-a-pair

        Update Speed: 3000ms OR 1000ms
        """
        self.live_subscribe(
            "{}@markPrice@{}s".format(pair.lower(), speed), id, callback, **kwargs
        )

    def kline(self, symbol: str, id: int, interval: str, callback, **kwargs):
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

        self.live_subscribe(
            "{}@kline_{}".format(symbol.lower(), interval), id, callback, **kwargs
        )

    def continuous_kline(
        self, pair: str, id: int, contractType: str, interval: str, callback, **kwargs
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

        self.live_subscribe(
            "{}_{}@continuousKline_{}".format(pair.lower(), contractType, interval),
            id,
            callback,
            **kwargs
        )

    def index_kline(self, pair: str, id: int, interval: str, callback, **kwargs):
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

        self.live_subscribe(
            "{}@indexPriceKline_{}".format(pair.lower(), interval),
            id,
            callback,
            **kwargs
        )

    def mark_kline(self, symbol: str, id: int, interval: str, callback, **kwargs):
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

        self.live_subscribe(
            "{}@markPriceKline_{}".format(symbol.lower(), interval),
            id,
            callback,
            **kwargs
        )

    def mini_ticker(self, id: int, callback, symbol=None, **kwargs):
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
            self.live_subscribe("!miniTicker@arr", id, callback, **kwargs)
        else:
            self.live_subscribe(
                "{}@miniTicker".format(symbol.lower()), id, callback, **kwargs
            )

    def ticker(self, id: int, callback, symbol=None, **kwargs):
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
            self.live_subscribe("!ticker@arr", id, callback, **kwargs)
        else:
            self.live_subscribe(
                "{}@ticker".format(symbol.lower()), id, callback, **kwargs
            )

    def book_ticker(self, id: int, callback, symbol=None, **kwargs):
        """Individual symbol or all book ticker

        Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol.

        Stream Name: <symbol>@bookTicker or
        Stream Name: !bookTicker

        https://binance-docs.github.io/apidocs/delivery/en/#individual-symbol-book-ticker-streams
        https://binance-docs.github.io/apidocs/delivery/en/#all-book-tickers-stream

        Update Speed: Real-time
        """

        if symbol is None:
            self.live_subscribe("!bookTicker", id, callback, **kwargs)
        else:
            self.live_subscribe(
                "{}@bookTicker".format(symbol.lower()), id, callback, **kwargs
            )

    def liquidation_order(self, id: int, callback, symbol=None, **kwargs):
        """The Liquidation Order Snapshot Streams push force liquidation order information for specific symbol.
        The All Liquidation Order Snapshot Streams push force liquidation order information for all symbols in the market.

        For each symbol，only the latest one liquidation order within 1000ms will be pushed as the snapshot. If no liquidation happens in the interval of 1000ms, no stream will be pushed.

        Stream Name: <symbol>@forceOrder or !forceOrder@arr

        https://binance-docs.github.io/apidocs/delivery/en/#liquidation-order-streams
        https://binance-docs.github.io/apidocs/delivery/en/#all-market-liquidation-order-streams

        Update Speed: 1000ms
        """
        if symbol is None:
            self.live_subscribe("!forceOrder@arr", id, callback, **kwargs)
        else:
            self.live_subscribe(
                "{}@forceOrder".format(symbol.lower()), id, callback, **kwargs
            )

    def partial_book_depth(
        self, symbol: str, id: int, level, speed, callback, **kwargs
    ):
        """Partial Book Depth Streams

        Top bids and asks, Valid are 5, 10, or 20.

        Stream Names: <symbol>@depth<levels> OR <symbol>@depth<levels>@500ms OR <symbol>@depth<levels>@100ms

        https://binance-docs.github.io/apidocs/delivery/en/#partial-book-depth-streams

        Update Speed: 250ms, 500ms or 100ms
        """

        self.live_subscribe(
            "{}@depth{}@{}ms".format(symbol.lower(), level, speed),
            id,
            callback,
            **kwargs
        )

    def diff_book_depth(self, symbol: str, id: int, speed, callback, **kwargs):
        """Diff. Depth Stream
        Order book price and quantity depth updates used to locally manage an order book.

        Stream Name: <symbol>@depth OR <symbol>@depth@500ms OR<symbol>@depth@100ms

        https://binance-docs.github.io/apidocs/delivery/en/#diff-book-depth-streams

        Update Speed: 250ms, 500ms or 100ms
        """

        self.live_subscribe(
            "{}@depth@{}ms".format(symbol.lower(), speed), id, callback, **kwargs
        )

    def user_data(self, listen_key: str, id: int, callback, **kwargs):
        """listen to user data by provided listenkey"""
        self.live_subscribe(listen_key, id, callback, **kwargs)
