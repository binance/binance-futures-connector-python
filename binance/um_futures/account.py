from binance.lib.utils import check_required_parameter, convert_list_to_json_array
from binance.lib.utils import check_required_parameters


def change_position_mode(self, dualSidePosition: str, **kwargs):
    """
    |
    | **Change Position Mode (TRADE)**
    | *Change user's position mode (Hedge Mode or One-way Mode) on EVERY symbol*

    :API endpoint: ``POST /fapi/v1/positionSide/dual``
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Position-Mode

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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Current-Position-Mode

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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Multi-Assets-Mode

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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode

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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api

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
    :parameter newOrderRespType: optional string. "ACK" or "RESULT", default "ACK".
    :parameter priceMatch: optional string. only avaliable for "LIMIT"/"STOP"/"TAKE_PROFIT" order; can be set to "OPPONENT"/"OPPONENT_5"/"OPPONENT_10"/"OPPONENT_20": /"QUEUE"/"QUEUE_5"/"QUEUE_10"/"QUEUE_20"; Can't be passed together with price.
    :parameter selfTradePreventionMode: optional string. "NONE":No STP /"EXPIRE_TAKER":expire taker order when STP triggers/"EXPIRE_MAKER":expire taker order when STP triggers/"EXPIRE_BOTH":expire both orders when STP triggers; default "NONE".
    :parameter goodTillDate: optional int. order cancel time for timeInForce "GTD", mandatory when timeInforce set to "GTD"; order the timestamp only retains second-level precision, ms part will be ignored; The goodTillDate timestamp must be greater than the current time plus 600 seconds and smaller than 253402300799000.
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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/New-Order-Test

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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Order

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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Place-Multiple-Orders

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
    :parameter newOrderRespType: optional string. "ACK" or "RESULT", default "ACK".
    :parameter priceMatch: optional string. only avaliable for "LIMIT"/"STOP"/"TAKE_PROFIT" order; can be set to "OPPONENT"/"OPPONENT_5"/"OPPONENT_10"/"OPPONENT_20": /"QUEUE"/"QUEUE_5"/"QUEUE_10"/"QUEUE_20"; Can't be passed together with price.
    :parameter selfTradePreventionMode: optional string. "NONE":No STP /"EXPIRE_TAKER":expire taker order when STP triggers/"EXPIRE_MAKER":expire taker order when STP triggers/"EXPIRE_BOTH":expire both orders when STP triggers; default "NONE".
    :parameter goodTillDate: optional int. order cancel time for timeInForce "GTD", mandatory when timeInforce set to "GTD"; order the timestamp only retains second-level precision, ms part will be ignored; The goodTillDate timestamp must be greater than the current time plus 600 seconds and smaller than 253402300799000.
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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Query-Order

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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Order

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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Open-Orders

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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Multiple-Orders

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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Auto-Cancel-All-Open-Orders

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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Query-Current-Open-Order

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
            ]
        ) 
        params = {"symbol": symbol}
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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Current-All-Open-Orders

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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/All-Orders

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

    :API endpoint: ``GET /fapi/v3/balance``
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V3

    :parameter recvWindow: optional int
    |
    """

    url_path = "/fapi/v3/balance"
    return self.sign_request("GET", url_path, {**kwargs})


def account(self, **kwargs):
    """
    |
    | **Account Information V3(USER_DATA)**
    | *Get current account information*

    :API endpoint: ``GET /fapi/v3/account``
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Account-Information-V3

    :parameter recvWindow: optional int
    |
    """

    url_path = "/fapi/v3/account"
    return self.sign_request("GET", url_path, {**kwargs})


def change_leverage(self, symbol: str, leverage: int, **kwargs):
    """
    |
    | **Change Initial Leverage (TRADE)**
    | *Change user's initial leverage of specific symbol market.*

    :API endpoint: ``POST /fapi/v1/leverage``
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage

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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Margin-Type

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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin

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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Get-Position-Margin-Change-History

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

    :API endpoint: ``GET /fapi/v3/positionRisk``
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V3

    :parameter symbol: string
    :parameter recvWindow: optional int
    |
    """

    url_path = "/fapi/v3/positionRisk"
    params = {**kwargs}

    return self.sign_request("GET", url_path, params)


def get_account_trades(self, symbol: str, **kwargs):
    """
    |
    | **Account Trade List (USER_DATA)**
    | *Get trades for a specific account and symbol.*

    :API endpoint: ``GET /fapi/v1/userTrades``
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Account-Trade-List

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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Income-History

    :parameter symbol: optional string
    :parameter incomeType: optional string; "TRANSFER", "WELCOME_BONUS", "REALIZED_PNL", "FUNDING_FEE", "COMMISSION" and "INSURANCE_CLEAR".
    :parameter startTime: optional int; timestamp in ms to get funding from INCLUSIVE.
    :parameter endTime: optional int; timestamp in ms to get funding from INCLUSIVE.
    :parameter page: optional int
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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets

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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Position-ADL-Quantile-Estimation

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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Users-Force-Orders

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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Futures-Trading-Quantitative-Rules-Indicators

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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate

    :parameter symbol: string
    :parameter recvWindow: optional int
    |
    """

    check_required_parameter(symbol, "symbol")
    url_path = "/fapi/v1/commissionRate"
    params = {"symbol": symbol, **kwargs}

    return self.sign_request("GET", url_path, params)


def futures_account_configuration(self, **kwargs):
    """
    |
    | **Futures Account Configuration(USER_DATA)**

    :API endpoint: ``GET /fapi/v1/accountConfig``
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Account-Config

    :parameter recvWindow: optional int
    |
    """
    url_path = "/fapi/v1/accountConfig"
    params = {**kwargs}

    return self.sign_request("GET", url_path, params)


def symbol_configuration(self, **kwargs):
    """
    |
    | **Symbol Configuration(USER_DATA)**
    | *Get current account symbol configuration.*

    :API endpoint: ``GET /fapi/v1/symbolConfig``
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Symbol-Config

    :parameter symbol: optional string
    :parameter recvWindow: optional int
    |
    """
    url_path = "/fapi/v1/symbolConfig"
    params = {**kwargs}

    return self.sign_request("GET", url_path, params)


def query_user_rate_limit(self, **kwargs):
    """
    |
    | **Query User Rate Limit (USER_DATA)**

    :API endpoint: ``GET /fapi/v1/rateLimit/order``
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Query-Rate-Limit

    :parameter recvWindow: optional int
    |
    """
    url_path = "/fapi/v1/rateLimit/order"
    params = {**kwargs}

    return self.sign_request("GET", url_path, params)


def download_transactions_asyn(self, startTime: int, endTime: int, **kwargs):
    """
    |
    | **Get Download Id For Futures Transaction History (USER_DATA)**

    :API endpoint: ``GET /fapi/v1/income/asyn``
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Transaction-History

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
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Futures-Transaction-History-Download-Link-by-Id

    :parameter downloadId:  string
    :parameter recvWindow: optional int
    |
    """

    check_required_parameter(downloadId, "downloadId")
    url_path = "/fapi/v1/income/asyn/id"
    params = {"downloadId": downloadId, **kwargs}

    return self.sign_request("GET", url_path, params)


def download_order_asyn(self, startTime: int, endTime: int, **kwargs):
    """
    |
    | **Get Download Id For Futures Order History (USER_DATA)**
    | *Request Limitation is 10 times per month, shared by front end download page and rest api*
    | *The time between startTime and endTime can not be longer than 1 year*

    :API endpoint: ``GET /fapi/v1/order/asyn``
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Order-History

    :parameter startTime:  int
    :parameter endTime:  int
    :parameter recvWindow: optional int
    |
    """

    check_required_parameter(startTime, "startTime")
    check_required_parameter(endTime, "endTime")
    url_path = "/fapi/v1/order/asyn"
    params = {"startTime": startTime, "endTime": endTime, **kwargs}

    return self.sign_request("GET", url_path, params)


def async_download_order_id(self, downloadId: str, **kwargs):
    """
    |
    | **Get Futures Order History Download Link by Id (USER_DATA)**
    | *Download link expiration: 24h*

    :API endpoint: ``GET /fapi/v1/order/asyn/id``
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Futures-Order-History-Download-Link-by-Id

    :parameter downloadId:  string
    :parameter recvWindow: optional int
    |
    """

    check_required_parameter(downloadId, "downloadId")
    url_path = "/fapi/v1/order/asyn/id"
    params = {"downloadId": downloadId, **kwargs}

    return self.sign_request("GET", url_path, params)


def download_trade_asyn(self, startTime: int, endTime: int, **kwargs):
    """
    |
    | **Get Download Id For Futures Trade History (USER_DATA)**
    | *Request Limitation is 5 times per month, shared by front end download page and rest api*
    | *The time between startTime and endTime can not be longer than 1 year*

    :API endpoint: ``GET /fapi/v1/trade/asyn``
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Trade-History

    :parameter startTime:  int
    :parameter endTime:  int
    :parameter recvWindow: optional int
    |
    """

    check_required_parameter(startTime, "startTime")
    check_required_parameter(endTime, "endTime")
    url_path = "/fapi/v1/trade/asyn"
    params = {"startTime": startTime, "endTime": endTime, **kwargs}

    return self.sign_request("GET", url_path, params)


def async_download_trade_id(self, downloadId: str, **kwargs):
    """
    |
    | **Get Futures Trade Download Link by Id(USER_DATA)**
    | *Download link expiration: 24h*

    :API endpoint: ``GET /fapi/v1/trade/asyn/id``
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Futures-Trade-Download-Link-by-Id

    :parameter downloadId:  string
    :parameter recvWindow: optional int
    |
    """

    check_required_parameter(downloadId, "downloadId")
    url_path = "/fapi/v1/trade/asyn/id"
    params = {"downloadId": downloadId, **kwargs}

    return self.sign_request("GET", url_path, params)


def toggle_bnb_burn(self, feeBurn: str, **kwargs):
    """
    |
    | **Toggle BNB Burn On Futures Trade (TRADE)**
    | *Change user's BNB Fee Discount (Fee Discount On or Fee Discount Off ) on EVERY symbol*

    :API endpoint: ``POST /fapi/v1/feeBurn``
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Toggle-BNB-Burn-On-Futures-Trade

    :parameter feeBurn: string; "true": Fee Discount On; "false": Fee Discount Off
    :parameter recvWindow: optional int
    |
    """

    check_required_parameter(feeBurn, "feeBurn")
    url_path = "/fapi/v1/feeBurn"
    params = {"feeBurn": feeBurn, **kwargs}

    return self.sign_request("POST", url_path, params)


def get_bnb_burn(self, **kwargs):
    """
    |
    | **Get BNB Burn Status (USER_DATA)**

    :API endpoint: ``GET /fapi/v1/feeBurn``
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-BNB-Burn-Status

    :parameter recvWindow: optional int
    |
    """

    url_path = "/fapi/v1/feeBurn"
    params = {**kwargs}

    return self.sign_request("GET", url_path, params)
