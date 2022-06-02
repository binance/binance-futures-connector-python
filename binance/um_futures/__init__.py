from binance.api import API


class UMFutures(API):
    def __init__(self, key=None, secret=None, **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = "https://fapi.binance.com"
        super().__init__(key, secret, **kwargs)

    # MARKETS
    from binance.um_futures.market import ping
    from binance.um_futures.market import time
    from binance.um_futures.market import exchange_info
    from binance.um_futures.market import depth
    from binance.um_futures.market import trades
    from binance.um_futures.market import historical_trades
    from binance.um_futures.market import agg_trades
    from binance.um_futures.market import klines
    from binance.um_futures.market import continuous_klines
    from binance.um_futures.market import index_price_klines
    from binance.um_futures.market import mark_price_klines
    from binance.um_futures.market import mark_price
    from binance.um_futures.market import funding_rate
    from binance.um_futures.market import ticker_24hr_price_change
    from binance.um_futures.market import ticker_price
    from binance.um_futures.market import book_ticker
    from binance.um_futures.market import open_interest
    from binance.um_futures.market import open_interest_hist
    from binance.um_futures.market import top_long_short_position_ratio
    from binance.um_futures.market import long_short_account_ratio
    from binance.um_futures.market import top_long_short_account_ratio
    from binance.um_futures.market import taker_long_short_ratio
    from binance.um_futures.market import blvt_kline
    from binance.um_futures.market import index_info
    from binance.um_futures.market import asset_Index

    # ACCOUNT(including orders and trades)
    from binance.um_futures.account import change_position_mode
    from binance.um_futures.account import get_position_mode
    from binance.um_futures.account import change_multi_asset_mode
    from binance.um_futures.account import get_multi_asset_mode
    from binance.um_futures.account import new_order
    from binance.um_futures.account import new_order_test
    from binance.um_futures.account import new_batch_order
    from binance.um_futures.account import query_order
    from binance.um_futures.account import cancel_order
    from binance.um_futures.account import cancel_open_orders
    from binance.um_futures.account import cancel_batch_order
    from binance.um_futures.account import countdown_cancel_order
    from binance.um_futures.account import get_open_orders
    from binance.um_futures.account import get_orders
    from binance.um_futures.account import get_all_orders
    from binance.um_futures.account import balance
    from binance.um_futures.account import account
    from binance.um_futures.account import change_leverage
    from binance.um_futures.account import change_margin_type
    from binance.um_futures.account import modify_isolated_position_margin
    from binance.um_futures.account import get_position_margin_history
    from binance.um_futures.account import get_position_risk
    from binance.um_futures.account import get_account_trades
    from binance.um_futures.account import get_income_history
    from binance.um_futures.account import leverage_brackets
    from binance.um_futures.account import adl_quantile
    from binance.um_futures.account import force_orders
    from binance.um_futures.account import api_trading_status
    from binance.um_futures.account import commission_rate
    from binance.um_futures.account import download_transactions_asyn
    from binance.um_futures.account import aysnc_download_info

    # STREAMS
    from binance.um_futures.data_stream import new_listen_key
    from binance.um_futures.data_stream import renew_listen_key
    from binance.um_futures.data_stream import close_listen_key
