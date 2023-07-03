from binance.lib.utils import check_required_parameter, convert_list_to_json_array
from binance.lib.utils import check_required_parameters


def change_position_mode(self, dualSidePosition: str, **kwargs):
    """
    |
    | **Change Position Mode (TRADE)**
    | *Change user's position mode (Hedge Mode or One-way Mode) on EVERY symbol*

    :API endpoint: ``POST /fapi/v1/positionSide/dual``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#change-position-mode-trade

    :parameter dualSidePosition: string
    :parameter recvWindow: optional int
    |
    """

    check_required_parameter(dualSidePosition, "dualSidePosition")
    params = {"dualSidePosition": dualSidePosition, **kwargs}
    url_path = "/fapi/v1/positionSide/dual"
    return self.sign_request("POST", url_path, params)


def get_position_mode(self, **kwargs):
    """
    |
    | **Get Current Position Mode (USER_DATA)**
    | *Get user's position mode (Hedge Mode or One-way Mode) on EVERY symbol*

    :API endpoint: ``GET /fapi/v1/positionSide/dual``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#get-current-position-mode-user_data

    :parameter recvWindow: optional int
    |
    """

    params = {**kwargs}
    url_path = "/fapi/v1/positionSide/dual"
    return self.sign_request("GET", url_path, params)


def change_multi_asset_mode(self, multiAssetsMargin: str, **kwargs):
    """
    |
    | **Change Multi-Assets Mode (TRADE)**
    | *Change user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on Every symbol*

    :API endpoint: ``POST /fapi/v1/multiAssetsMargin``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#change-multi-assets-mode-trade

    :parameter multiAssetsMargin: string; "true": Multi-Assets Mode; "false": Single-Asset Mode
    :parameter recvWindow: optional int
    |
    """

    check_required_parameter(multiAssetsMargin, "multiAssetsMargin")
    params = {"multiAssetsMargin": multiAssetsMargin, **kwargs}
    url_path = "/fapi/v1/multiAssetsMargin"
    return self.sign_request("POST", url_path, params)


def get_multi_asset_mode(self, **kwargs):
    """
    |
    | **Get Current Multi-Assets Mode (USER_DATA)**
    | *Get user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on Every symbol*

    :API endpoint: ``GET /fapi/v1/multiAssetsMargin``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#get-current-multi-assets-mode-user_data

    :parameter recvWindow: optional int
    |
    """

    params = {**kwargs}
    url_path = "/fapi/v1/multiAssetsMargin"
    return self.sign_request("GET", url_path, params)


def new_order(self, symbol: str, side: str, type: str, **kwargs):
    """
    |
    | **New Order (TRADE)**
    | *Send a new order*

    :API endpoint: ``POST /fapi/v1/order``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#new-order-trade

    :parameter symbol: string
    :parameter side: string
    :parameter type: string
    :parameter positionSide: optional string. Default BOTH for One-way Mode; LONG or SHORT for Hedge Mode. It must be passed in Hedge Mode.
    :parameter timeInForce: optional string
    :parameter quantity: optional float
    :parameter reduceOnly: optional string
    :parameter price: optional float
    :parameter newClientOrderId: optional string. An unique ID among open orders. Automatically generated if not sent.
    :parameter stopPrice: optional float. Use with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
    :parameter closePosition: optional string. true or false; Close-All, use with STOP_MARKET or TAKE_PROFIT_MARKET.
    :parameter activationPrice: optional float. Use with TRAILING_STOP_MARKET orders, default is the latest price (supporting different workingType).
    :parameter callbackRate: optional float. Use with TRAILING_STOP_MARKET orders, min 0.1, max 5 where 1 for 1%.
    :parameter workingType: optional string. stopPrice triggered by: "MARK_PRICE", "CONTRACT_PRICE". Default "CONTRACT_PRICE".
    :parameter priceProtect: optional string. "TRUE" or "FALSE", default "FALSE". Use with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
    :parameter newOrderRespType: optional float. "ACK" or "RESULT", default "ACK".
    :parameter recvWindow: optional int
    |
    """

    check_required_parameters([[symbol, "symbol"], [side, "side"], [type, "type"]])
    params = {"symbol": symbol, "side": side, "type": type, **kwargs}
    url_path = "/fapi/v1/order"
    return self.sign_request("POST", url_path, params)


def new_order_test(self, symbol: str, side: str, type: str, **kwargs):
    """
    |
    | **New Test Order (TRADE)**
    | *Send a new test order*

    :API endpoint: ``POST /fapi/v1/order/test``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#new-order-trade

    :parameter symbol: string
    :parameter side: string
    :parameter type: string
    :parameter positionSide: optional string. Default BOTH for One-way Mode; LONG or SHORT for Hedge Mode. It must be passed in Hedge Mode.
    :parameter timeInForce: optional string
    :parameter quantity: optional float
    :parameter reduceOnly: optional string
    :parameter price: optional float
    :parameter newClientOrderId: optional string. An unique ID among open orders. Automatically generated if not sent.
    :parameter stopPrice: optional float. Use with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
    :parameter closePosition: optional string. true or false; Close-All, use with STOP_MARKET or TAKE_PROFIT_MARKET.
    :parameter activationPrice: optional float. Use with TRAILING_STOP_MARKET orders, default is the latest price (supporting different workingType).
    :parameter callbackRate: optional float. Use with TRAILING_STOP_MARKET orders, min 0.1, max 5 where 1 for 1%.
    :parameter workingType: optional string. stopPrice triggered by: "MARK_PRICE", "CONTRACT_PRICE". Default "CONTRACT_PRICE".
    :parameter priceProtect: optional string. "TRUE" or "FALSE", default "FALSE". Use with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
    :parameter newOrderRespType: optional float. "ACK" or "RESULT", default "ACK".
    :parameter recvWindow: optional int
    |
    """

    check_required_parameters([[symbol, "symbol"], [side, "side"], [type, "type"]])
    params = {"symbol": symbol, "side": side, "type": type, **kwargs}
    url_path = "/fapi/v1/order/test"
    return self.sign_request("POST", url_path, params)


def modify_order(
    self,
    symbol: str,
    side: str,
    quantity: float,
    price: float,
    orderId: int = None,
    origClientOrderId: str = None,
    **kwargs
):
    """
    |
    | **Modify Order (TRADE)**
    | *Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered in the match queue*

    :API endpoint: ``PUT /fapi/v1/order``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#modify-order-trade

    :parameter symbol: string
    :parameter side: string
    :parameter quantity: float
    :parameter price: float
    :parameter orderId: optional int
    :parameter origClientOrderId: optional string. Either orderId or origClientOrderId must be sent, and the orderId will prevail if both are sent.
    :parameter recvWindow: optional int
    |
    """
    check_required_parameters(
        [
            [symbol, "symbol"],
            [side, "side"],
            [quantity, "quantity"],
            [price, "price"],
        ]
    )
    if (orderId is None) and (origClientOrderId is None):
        check_required_parameters(
            [
                [orderId, "orderId"],
            ]
        )
    elif orderId:
        params = {
            "symbol": symbol,
            "side": side,
            "quantity": quantity,
            "orderId": orderId,
            "price": price,
            **kwargs,
        }
    else:
        params = {
            "symbol": symbol,
            "side": side,
            "quantity": quantity,
            "origClientOrderId": origClientOrderId,
            "price": price,
            **kwargs,
        }

    url_path = "/fapi/v1/order"
    return self.sign_request("PUT", url_path, params)


def new_batch_order(self, batchOrders: list):
    """
    |
    | **Place Multiple Orders (TRADE)**
    | *Post a new batch order*

    :API endpoint: ``POST /fapi/v1/batchOrders``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#place-multiple-orders-trade

    :parameter symbol: string
    :parameter side: string
    :parameter type: string
    :parameter positionSide: optional string. Default BOTH for One-way Mode; LONG or SHORT for Hedge Mode. It must be passed in Hedge Mode.
    :parameter timeInForce: optional string
    :parameter quantity: optional float
    :parameter reduceOnly: optional string
    :parameter price: optional float
    :parameter newClientOrderId: optional string. An unique ID among open orders. Automatically generated if not sent.
    :parameter stopPrice: optional float. Use with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
    :parameter closePosition: optional string. true or false; Close-All, use with STOP_MARKET or TAKE_PROFIT_MARKET.
    :parameter activationPrice: optional float. Use with TRAILING_STOP_MARKET orders, default is the latest price (supporting different workingType).
    :parameter callbackRate: optional float. Use with TRAILING_STOP_MARKET orders, min 0.1, max 5 where 1 for 1%.
    :parameter workingType: optional string. stopPrice triggered by: "MARK_PRICE", "CONTRACT_PRICE". Default "CONTRACT_PRICE".
    :parameter priceProtect: optional string. "TRUE" or "FALSE", default "FALSE". Use with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
    :parameter newOrderRespType: optional float. "ACK" or "RESULT", default "ACK".
    :parameter recvWindow: optional int
    |

    **Notes**
        - Batch orders are processed concurrently, and the order of matching is not guaranteed.
        - The order of returned contents for batch orders is the same as the order of the order list.
            - batchOrders (list): order list. Max 5 orders
        - batchOrders is the list of order parameters in JSON

        - example:
            batchOrders = {
                "batchOrders": [
                    {
                        "symbol":"BTCUSDT",
                        "side": "SELL",
                        "type": "LIMIT",
                        "quantity": "0.001",
                        "timeInForce": "GTC",
                        "reduceOnly": "false",
                        "price": "9563.51"
                    },
                    {
                        "symbol":"BTCUSDT",
                        "side": "SELL",
                        "type": "LIMIT",
                        "quantity": "0.001",
                        "timeInForce": "GTC",
                        "reduceOnly": "false",
                        "price": "9613.51"
                    }
                    ]
                }
    |
    """

    params = {"batchOrders": batchOrders}
    url_path = "/fapi/v1/batchOrders"
    return self.sign_request("POST", url_path, params, True)


def query_order(
    self, symbol: str, orderId: int = None, origClientOrderId: str = None, **kwargs
):
    """
    |
    | **Query Order (USER_DATA)**
    | *Check an order's status*

    :API endpoint: ``GET /fapi/v1/order``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#query-order-user_data

    :parameter symbol: string
    :parameter orderId: optional int
    :parameter origClientOrderId: optional string
    :parameter recvWindow: optional int
    |
    """

    if (orderId is None) and (origClientOrderId is None):
        check_required_parameters(
            [
                [symbol, "symbol"],
                [orderId, "orderId"],
                ["origClientOrderId", origClientOrderId],
            ]
        )
    elif orderId:
        params = {"symbol": symbol, "orderId": orderId, **kwargs}
    else:
        params = {"symbol": symbol, "origClientOrderId": origClientOrderId, **kwargs}

    url_path = "/fapi/v1/order"
    return self.sign_request("GET", url_path, params)


def cancel_order(
    self, symbol: str, orderId: int = None, origClientOrderId: str = None, **kwargs
):
    """
    |
    | **Cancel Order (TRADE)**
    | *Cancel an active order.*

    :API endpoint: ``DELETE /fapi/v1/order``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#cancel-order-trade

    :parameter symbol: string
    :parameter orderId: optional int
    :parameter origClientOrderId: optional string
    :parameter newClientOrderId: optional string
    :parameter recvWindow: optional int
    |
    """

    if (orderId is None) and (origClientOrderId is None):
        check_required_parameters(
            [
                [symbol, "symbol"],
                [orderId, "orderId"],
                ["origClientOrderId", origClientOrderId],
            ]
        )
    elif orderId:
        params = {"symbol": symbol, "orderId": orderId, **kwargs}
    else:
        params = {"symbol": symbol, "origClientOrderId": origClientOrderId, **kwargs}

    url_path = "/fapi/v1/order"
    return self.sign_request("DELETE", url_path, params)


def cancel_open_orders(self, symbol: str, **kwargs):
    """
    |
    | **Cancel All Open Orders (TRADE)**

    :API endpoint: ``DELETE /fapi/v1/allOpenOrders``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#cancel-all-open-orders-trade

    :parameter symbol: string
    :parameter recvWindow: optional int; the value cannot be greater than 60000.
    |
    """

    url_path = "/fapi/v1/allOpenOrders"
    params = {"symbol": symbol, **kwargs}

    return self.sign_request("DELETE", url_path, params)


def cancel_batch_order(
    self, symbol: str, orderIdList: list, origClientOrderIdList: list, **kwargs
):
    """
    |
    | **Cancel Multiple Orders (TRADE)**
    | *Cancel a new batch order*

    :API endpoint: ``DELETE /fapi/v1/batchOrders``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#cancel-multiple-orders-trade

    :parameter symbol: string
    :parameter orderIdList: int list; max length 10 e.g. [1234567, 2345678]
    :parameter origClientOrderIdList: string list; max length 10 e.g. ["my_id_1", "my_id_2"], encode the double quotes. No space after comma.
    :parameter recvWindow: optional int

    **Notes**
        - Either orderIdList or origClientOrderIdList must be sent.
    |
    """

    url_path = "/fapi/v1/batchOrders"
    params = {}

    if (orderIdList is None) and (origClientOrderIdList is None):
        check_required_parameters(
            [
                [symbol, "symbol"],
                [orderIdList, "orderIdList"],
                [origClientOrderIdList, "origClientOrderIdList"],
            ]
        )
    elif orderIdList:
        params = {
            "symbol": symbol,
            "orderIdList": convert_list_to_json_array(orderIdList),
            **kwargs,
        }
    else:
        params = {
            "symbol": symbol,
            "origClientOrderIdList": convert_list_to_json_array(origClientOrderIdList),
            **kwargs,
        }

    return self.sign_request("DELETE", url_path, params)


def countdown_cancel_order(self, symbol: str, countdownTime: int, **kwargs):
    """
    |
    | **Auto-Cancel All Open Orders (TRADE)**
    | *Cancel all open orders of the specified symbol at the end of the specified countdown.*

    :API endpoint: ``POST /fapi/v1/countdownCancelAll``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#auto-cancel-all-open-orders-trade

    :parameter symbol: string
    :parameter countdownTime: int list; countdown time, 1000 for 1 second. 0 to cancel the timer.
    :parameter recvWindow: optional int

    **Notes**
        - The endpoint should be called repeatedly as heartbeats so that the existing countdown time can be canceled and replaced by a new one.
        - Example usage:
            - Call this endpoint at 30s intervals with an countdownTime of 120000 (120s).
            - If this endpoint is not called within 120 seconds, all your orders of the specified symbol will be automatically canceled.
            - If this endpoint is called with an countdownTime of 0, the countdown timer will be stopped.
        - The system will check all countdowns approximately every 10 milliseconds, so please note that sufficient redundancy should be considered when using this function.
        - We do not recommend setting the countdown time to be too precise or too small.
    """

    check_required_parameters([[symbol, "symbol"], [countdownTime, "countdownTime"]])
    url_path = "/fapi/v1/countdownCancelAll"
    params = {"symbol": symbol, "countdownTime": countdownTime, **kwargs}

    return self.sign_request("POST", url_path, params)


def get_open_orders(
    self, symbol: str, orderId: int = None, origClientOrderId: str = None, **kwargs
):
    """
    |
    | **Query Current Open Order (USER_DATA)**
    | *Get all open orders on a symbol.*

    :API endpoint: ``GET /fapi/v1/openOrder``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#query-current-open-order-user_data

    :parameter symbol: string
    :parameter orderId: optional int
    :parameter origClientOrderId: optional int
    :parameter recvWindow: optional int; the value cannot be greater than 60000.

    **Notes**
        - Either orderId or origClientOrderId must be sent
        - If the queried order has been filled or cancelled, the error message "Order does not exist" will be returned.
    """

    url_path = "/fapi/v1/openOrder"
    params = {}

    if (orderId is None) and (origClientOrderId is None):
        check_required_parameters(
            [
                [symbol, "symbol"],
                [orderId, "orderId"],
                [origClientOrderId, "origClientOrderId"],
            ]
        )
    elif orderId:
        params = {"symbol": symbol, "orderId": orderId, **kwargs}
    else:
        params = {"symbol": symbol, "origClientOrderId": origClientOrderId, **kwargs}

    return self.sign_request("GET", url_path, params)


def get_orders(self, **kwargs):
    """
    |
    | **Current All Open Orders (USER_DATA)**
    | *Get all open orders on a symbol. Careful when accessing this with no symbol.*
    | *If the symbol is not sent, orders for all symbols will be returned in an array.*

    :API endpoint: ``GET /fapi/v1/openOrders``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#current-all-open-orders-user_data

    :parameter symbol: optional string
    :parameter recvWindow: optional int; the value cannot be greater than 60000.
    |
    """

    url_path = "/fapi/v1/openOrders"
    params = {**kwargs}

    return self.sign_request("GET", url_path, params)


def get_all_orders(self, symbol: str, **kwargs):
    """
    |
    | **All Orders (USER_DATA)**
    | *Get all account orders; active, canceled, or filled.*

    :API endpoint: ``GET /fapi/v1/allOrders``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#all-orders-user_data

    :parameter symbol: string
    :parameter orderId: optional int
    :parameter startTime: optional int
    :parameter endTime: optional int
    :parameter limit: optional int
    :parameter recvWindow: optional int; the value cannot be greater than 60000.
    |
    """

    check_required_parameter(symbol, "symbol")
    url_path = "/fapi/v1/allOrders"
    params = {"symbol": symbol, **kwargs}

    return self.sign_request("GET", url_path, params)


def balance(self, **kwargs):
    """
    |
    | **Futures Account Balance V2 (USER_DATA)**
    | *Get current account balance*

    :API endpoint: ``GET /fapi/v2/balance``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#futures-account-balance-v2-user_data

    :parameter recvWindow: optional int
    |
    """

    url_path = "/fapi/v2/balance"
    return self.sign_request("GET", url_path, {**kwargs})


def account(self, **kwargs):
    """
    |
    | **Account Information V2 (USER_DATA)**
    | *Get current account information*

    :API endpoint: ``GET /fapi/v2/account``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#account-information-v2-user_data

    :parameter recvWindow: optional int
    |
    """

    url_path = "/fapi/v2/account"
    return self.sign_request("GET", url_path, {**kwargs})


def change_leverage(self, symbol: str, leverage: int, **kwargs):
    """
    |
    | **Change Initial Leverage (TRADE)**
    | *Change user's initial leverage of specific symbol market.*

    :API endpoint: ``POST /fapi/v1/leverage``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#change-initial-leverage-trade

    :parameter symbol: string
    :parameter leverage: int; target initial leverage: int from 1 to 125.
    :parameter recvWindow: optional int; the value cannot be greater than 60000.
    |
    """

    check_required_parameters([[symbol, "symbol"], [leverage, "leverage"]])
    url_path = "/fapi/v1/leverage"
    params = {"symbol": symbol, "leverage": leverage, **kwargs}
    return self.sign_request("POST", url_path, params)


def change_margin_type(self, symbol: str, marginType: str, **kwargs):
    """
    |
    | **Change margin type (TRADE)**
    | *Change user's margin type of specific symbol market.*

    :API endpoint: ``POST /fapi/v1/marginType``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#change-margin-type-trade

    :parameter symbol: string
    :parameter marginType: string; ISOLATED, CROSSED.
    :parameter recvWindow: optional int; the value cannot be greater than 60000.
    |
    """

    check_required_parameters([[symbol, "symbol"], [marginType, "marginType"]])

    url_path = "/fapi/v1/marginType"
    params = {"symbol": symbol, "marginType": marginType, **kwargs}
    return self.sign_request("POST", url_path, params)


def modify_isolated_position_margin(
    self, symbol: str, amount: float, type: int, **kwargs
):
    """
    |
    | **Modify Isolated Position Margin (TRADE)**

    :API endpoint: ``POST /fapi/v1/positionMargin``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#modify-isolated-position-margin-trade

    :parameter symbol: string
    :parameter amount: float
    :parameter type: int; 1: Add position margin, 2: Reduce position margin
    :parameter positionSide: optional string; default BOTH for One-way Mode, LONG or SHORT for Hedge Mode. It must be sent with Hedge Mode.
    :parameter recvWindow: optional int; the value cannot be greater than 60000.
    |
    """

    check_required_parameters([[symbol, "symbol"], [amount, "amount"], [type, "type"]])
    url_path = "/fapi/v1/positionMargin"
    params = {"symbol": symbol, "amount": amount, "type": type, **kwargs}
    return self.sign_request("POST", url_path, params)


def get_position_margin_history(self, symbol: str, **kwargs):
    """
    |
    | **Get Position Margin Change History (TRADE)**
    | *Get position margin history on a symbol.*

    :API endpoint: ``GET /fapi/v1/positionMargin/history``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#get-position-margin-change-history-trade

    :parameter symbol: string
    :parameter type: optional int; 1: Add position margin, 2: Reduce position margin.
    :parameter startTime: optional int
    :parameter endTime: optional int
    :parameter limit: optional int; default: 500.
    :parameter recvWindow: optional int
    |
    """

    check_required_parameter(symbol, "symbol")
    url_path = "/fapi/v1/positionMargin/history"
    params = {"symbol": symbol, **kwargs}

    return self.sign_request("GET", url_path, params)


def get_position_risk(self, **kwargs):
    """
    |
    | **Position Information V2 (USER_DATA)**
    | *Get current position information.*

    :API endpoint: ``GET /fapi/v2/positionRisk``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#position-information-v2-user_data

    :parameter symbol: string
    :parameter recvWindow: optional int
    |
    """

    url_path = "/fapi/v2/positionRisk"
    params = {**kwargs}

    return self.sign_request("GET", url_path, params)


def get_account_trades(self, symbol: str, **kwargs):
    """
    |
    | **Account Trade List (USER_DATA)**
    | *Get trades for a specific account and symbol.*

    :API endpoint: ``GET /fapi/v1/userTrades``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#account-trade-list-user_data

    :parameter symbol: string
    :parameter startTime: optional int
    :parameter endTime: optional int
    :parameter fromId: optional int; trade ID to fetch from, default gets most recent trades.
    :parameter limit: optional int; default: 500, max: 1000.
    :parameter recvWindow: optional int

    **Notes**
        - If startTime and endTime are both not sent, then the last 7 days' data will be returned.
        - The time between startTime and endTime cannot be longer than 7 days.
        - The parameter fromId cannot be sent with startTime or endTime.
    |
    """

    check_required_parameter(symbol, "symbol")
    url_path = "/fapi/v1/userTrades"
    params = {"symbol": symbol, **kwargs}

    return self.sign_request("GET", url_path, params)


def get_income_history(self, **kwargs):
    """
    |
    | **Get Income History (USER_DATA)**
    | *Get trades for a specific account and symbol.*

    :API endpoint: ``GET /fapi/v1/income``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#get-income-history-user_data

    :parameter symbol: optional string
    :parameter incomeType: optional string; "TRANSFER", "WELCOME_BONUS", "REALIZED_PNL", "FUNDING_FEE", "COMMISSION" and "INSURANCE_CLEAR".
    :parameter startTime: optional int; timestamp in ms to get funding from INCLUSIVE.
    :parameter endTime: optional int; timestamp in ms to get funding from INCLUSIVE.
    :parameter limit: optional int; default: 100, max: 1000.
    :parameter recvWindow: optional int

    **Notes**
        - If neither startTime nor endTime is sent, the recent 7-day data will be returned.
        - If incomeType is not sent, all kinds of flow will be returned
        - "trandId" is unique in the same incomeType for a user
    """

    url_path = "/fapi/v1/income"
    params = {**kwargs}
    return self.sign_request("GET", url_path, params)


def leverage_brackets(self, **kwargs):
    """
    |
    | **Notional and Leverage Brackets (USER_DATA)**
    | *Get notional and leverage bracket.*

    :API endpoint: ``GET /fapi/v1/leverageBracket``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#notional-and-leverage-brackets-user_data

    :parameter symbol: optional string
    :parameter recvWindow: optional int
    |
    """

    url_path = "/fapi/v1/leverageBracket"
    params = {**kwargs}

    return self.sign_request("GET", url_path, params)


def adl_quantile(self, **kwargs):
    """
    |
    | **Position ADL Quantile Estimation (USER_DATA)**
    | *Get Position ADL Quantile Estimation*

    :API endpoint: ``GET /fapi/v1/adlQuantile``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#position-adl-quantile-estimation-user_data

    :parameter symbol: optional string
    :parameter recvWindow: optional int

    **Notes**
        - Values update every 30s.
        - Values 0, 1, 2, 3, 4 shows the queue position and possibility of ADL from low to high.
        - For positions of the symbol are in One-way Mode or isolated margined in Hedge Mode, "LONG", "SHORT", and "BOTH" will be returned to show the positions' adl quantiles of different position sides.
        - If the positions of the symbol are crossed margined in Hedge Mode:
            - "HEDGE" as a sign will be returned instead of "BOTH"
        - A same value caculated on unrealized pnls on long and short sides' positions will be shown for "LONG" and "SHORT" when there are positions in both of long and short sides.
    |
    """

    url_path = "/fapi/v1/adlQuantile"
    params = {**kwargs}
    return self.sign_request("GET", url_path, params)


def force_orders(self, **kwargs):
    """
    |
    | **User's Force Orders (USER_DATA)**
    | *Get User's Force Orders*

    :API endpoint: ``GET /fapi/v1/forceOrders``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#user-39-s-force-orders-user_data

    :parameter symbol: optional string
    :parameter autoCloseType: optional string; "LIQUIDATION" for liquidation orders, "ADL" for ADL orders.
    :parameter startTime: optional int
    :parameter endTime: optional int
    :parameter Limit: optional int; default 50, max 100.
    :parameter recvWindow: optional int

    **Notes**
        - If "autoCloseType" is not sent, orders with both of the types will be returned
        - If "startTime" is not sent, data within 7 days before "endTime" can be queried
    |
    """

    url_path = "/fapi/v1/forceOrders"
    params = {**kwargs}

    return self.sign_request("GET", url_path, params)


def api_trading_status(self, **kwargs):
    """
    |
    | **User API Trading Quantitative Rules Indicators (USER_DATA)**
    | *Get User API Trading Quantitative Rules Indicators*

    :API endpoint: ``GET /fapi/v1/apiTradingStatus``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#user-api-trading-quantitative-rules-indicators-user_data

    :parameter symbol: optional string
    :parameter recvWindow: optional int
    |
    """

    url_path = "/fapi/v1/apiTradingStatus"
    params = {**kwargs}

    return self.sign_request("GET", url_path, params)


def commission_rate(self, symbol: str, **kwargs):
    """
    |
    | **User Commission Rate (USER_DATA)**
    | *Get commission rate of symbol*

    :API endpoint: ``GET /fapi/v1/commissionRate``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#user-commission-rate-user_data

    :parameter symbol: string
    :parameter recvWindow: optional int
    |
    """

    check_required_parameter(symbol, "symbol")
    url_path = "/fapi/v1/commissionRate"
    params = {"symbol": symbol, **kwargs}

    return self.sign_request("GET", url_path, params)


def download_transactions_asyn(self, startTime: int, endTime: int, **kwargs):
    """
    |
    | **Get Download Id For Futures Transaction History (USER_DATA)**

    :API endpoint: ``GET /fapi/v1/income/asyn``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#get-download-id-for-futures-transaction-history-user_data

    :parameter startTime:  int
    :parameter endTime:  int
    :parameter recvWindow: optional int
    |
    """

    check_required_parameter(startTime, "startTime")
    check_required_parameter(endTime, "endTime")
    url_path = "/fapi/v1/income/asyn"
    params = {"startTime": startTime, "endTime": endTime, **kwargs}

    return self.sign_request("GET", url_path, params)


def aysnc_download_info(self, downloadId: str, **kwargs):
    """
    |
    | **Get Futures Transaction History Download Link by Id (USER_DATA)**

    :API endpoint: ``GET /fapi/v1/income/asyn/id``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#get-futures-transaction-history-download-link-by-id-user_data

    :parameter downloadId:  string
    :parameter recvWindow: optional int
    |
    """

    check_required_parameter(downloadId, "downloadId")
    url_path = "/fapi/v1/income/asyn/id"
    params = {"downloadId": downloadId, **kwargs}

    return self.sign_request("GET", url_path, params)
