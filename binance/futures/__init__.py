from binance.api import API


class Futures(API):
    def __init__(self, key=None, secret=None, **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = "https://fapi.binance.com"
        super().__init__(key, secret, **kwargs)

    # MARKETS
    from binance.futures.market import ping
    from binance.futures.market import time
    from binance.futures.market import exchange_info
    from binance.futures.market import depth
    from binance.futures.market import trades
    from binance.futures.market import historical_trades
    from binance.futures.market import agg_trades
    from binance.futures.market import klines
    from binance.futures.market import continuous_klines
    from binance.futures.market import index_price_klines
    from binance.futures.market import mark_price_klines
    from binance.futures.market import mark_price
    from binance.futures.market import funding_rate
    from binance.futures.market import ticker_24hr_price_change
    from binance.futures.market import ticker_price
    from binance.futures.market import book_ticker
    from binance.futures.market import open_interest
    from binance.futures.market import open_interest_hist
    from binance.futures.market import top_long_short_position_ratio
    from binance.futures.market import long_short_account_ratio
    from binance.futures.market import top_long_short_account_ratio
    from binance.futures.market import taker_long_short_ratio
    from binance.futures.market import blvt_kline
    from binance.futures.market import index_info
    from binance.futures.market import asset_Index

    # ACCOUNT(including orders and trades)
    from binance.futures.account import change_position_mode
    from binance.futures.account import get_position_mode
    from binance.futures.account import change_multi_asset_mode
    from binance.futures.account import get_multi_asset_mode
    from binance.futures.account import new_order
    from binance.futures.account import new_order_test
    from binance.futures.account import new_batch_order
    from binance.futures.account import query_order
    from binance.futures.account import cancel_order
    from binance.futures.account import cancel_open_orders
    from binance.futures.account import cancel_batch_order
    from binance.futures.account import countdown_cancel_order
    from binance.futures.account import get_open_orders
    from binance.futures.account import get_orders
    from binance.futures.account import get_all_orders
    from binance.futures.account import balance
    from binance.futures.account import account
    from binance.futures.account import change_leverage
    from binance.futures.account import change_margin_type
    from binance.futures.account import modify_isolated_position_margin
    from binance.futures.account import get_position_margin_history
    from binance.futures.account import get_position_risk
    from binance.futures.account import get_account_trades
    from binance.futures.account import get_income_history
    from binance.futures.account import leverage_brackets
    from binance.futures.account import adl_quantile
    from binance.futures.account import force_orders
    from binance.futures.account import api_trading_status
    from binance.futures.account import commission_rate

    # STREAMS
    from binance.futures.data_stream import new_listen_key
    from binance.futures.data_stream import renew_listen_key
    from binance.futures.data_stream import close_listen_key
 


 
