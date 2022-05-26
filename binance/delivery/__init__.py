from binance.api import API


class Delivery(API):
    def __init__(self, key=None, secret=None, **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = "https://dapi.binance.com"
        super().__init__(key, secret, **kwargs)

    # MARKETS
    from binance.delivery.market import ping
    from binance.delivery.market import time
    from binance.delivery.market import exchange_info
    from binance.delivery.market import depth
    from binance.delivery.market import trades
    from binance.delivery.market import historical_trades
    from binance.delivery.market import agg_trades
    from binance.delivery.market import klines
    from binance.delivery.market import continuous_klines
    from binance.delivery.market import index_price_klines
    from binance.delivery.market import mark_price_klines
    from binance.delivery.market import mark_price
    from binance.delivery.market import funding_rate
    from binance.delivery.market import ticker_24hr_price_change
    from binance.delivery.market import ticker_price
    from binance.delivery.market import book_ticker
    from binance.delivery.market import open_interest
    from binance.delivery.market import open_interest_hist
    from binance.delivery.market import top_long_short_account_ratio
    from binance.delivery.market import top_long_short_position_ratio
    from binance.delivery.market import long_short_account_ratio
    from binance.delivery.market import taker_long_short_ratio
    from binance.delivery.market import basis

    # ACCOUNT(including orders and trades)
    from binance.delivery.account import change_position_mode
    from binance.delivery.account import get_position_mode
    from binance.delivery.account import new_order
    from binance.delivery.account import modify_order
    from binance.delivery.account import new_batch_order
    from binance.delivery.account import modify_batch_order
    from binance.delivery.account import order_modify_history
    from binance.delivery.account import query_order
    from binance.delivery.account import cancel_order
    from binance.delivery.account import cancel_open_orders
    from binance.delivery.account import cancel_batch_order
    from binance.delivery.account import countdown_cancel_order
    from binance.delivery.account import get_open_orders
    from binance.delivery.account import get_orders
    from binance.delivery.account import get_all_orders
    from binance.delivery.account import balance
    from binance.delivery.account import account
    from binance.delivery.account import change_leverage
    from binance.delivery.account import change_margin_type
    from binance.delivery.account import modify_isolated_position_margin
    from binance.delivery.account import get_position_margin_history
    from binance.delivery.account import get_position_risk
    from binance.delivery.account import get_account_trades
    from binance.delivery.account import get_income_history
    from binance.delivery.account import leverage_brackets
    from binance.delivery.account import adl_quantile
    from binance.delivery.account import force_orders
    from binance.delivery.account import commission_rate

    # STREAMS
    from binance.delivery.data_stream import new_listen_key
    from binance.delivery.data_stream import renew_listen_key
    from binance.delivery.data_stream import close_listen_key
