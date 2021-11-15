from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters


def change_position_mode(self, dualSidePosition: str, **kwargs):
    """Change Position Mode(TRADE)

    Change user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol

    POST /dapi/v1/positionSide/dual

    https://binance-docs.github.io/apidocs/delivery/en/#change-position-mode-trade

    Args:
        dualSidePosition (str)
    Keyword Args:
        recvWindow (int, optional)
    """

    check_required_parameter(dualSidePosition, "dualSidePosition")
    params = {"dualSidePosition": dualSidePosition, **kwargs}
    url_path = "/dapi/v1/positionSide/dual"
    return self.sign_request("POST", url_path, params)


def get_position_mode(self, **kwargs):
    """Get Current Position Mode(USER_DATA)

    Get user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol

    GET /dapi/v1/positionSide/dual

    https://binance-docs.github.io/apidocs/delivery/en/#get-current-position-mode-user_data

    Args:
    Keyword Args:
        recvWindow (int, optional)
    """

    params = {**kwargs}
    url_path = "/dapi/v1/positionSide/dual"
    return self.sign_request("GET", url_path, params)


def new_order(self, symbol: str, side: str, type: str, **kwargs):
    """New Order (TRADE)

    Send a new order

    POST /dapi/v1/order

    https://binance-docs.github.io/apidocs/delivery/en/#new-order-trade

    Args:
        symbol (str)
        side (str)
        type (str)
    Keyword Args:
        positionSide (str, optional): Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode.
        timeInForce (str, optional)
        quantity (float, optional)
        reduceOnly (str, optional): "true" or "false". default "false". Cannot be sent in Hedge Mode; cannot be sent with closePosition=true
        price (float, optional)
        newClientOrderId (str, optional): A unique id among open orders. Automatically generated if not sent.
        stopPrice (float, optional): Used with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
        closePosition (str, optional): true, false；Close-All，used with STOP_MARKET or TAKE_PROFIT_MARKET.
        activationPrice (float, optional): Used with TRAILING_STOP_MARKET orders, default as the latest price(supporting different workingType).
        callbackRate (float, optional): Used with TRAILING_STOP_MARKET orders, min 0.1, max 5 where 1 for 1%.
        workingType (str, optional): stopPrice triggered by: "MARK_PRICE", "CONTRACT_PRICE". Default "CONTRACT_PRICE".
        priceProtect (str, optional): "TRUE" or "FALSE", default "FALSE". Used with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
        newOrderRespType (str, optional): "ACK", "RESULT", default "ACK"
        recvWindow (int, optional)
    """

    check_required_parameters([[symbol, "symbol"], [side, "side"], [type, "type"]])
    params = {"symbol": symbol, "side": side, "type": type, **kwargs}
    url_path = "/dapi/v1/order"
    return self.sign_request("POST", url_path, params)


def modify_order(self, symbol: str, side: str, orderId: int = None, origClientOrderId: str = None, **kwargs):
    """Modify Order(TRADE)

    Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered in the match queue

    POST /dapi/v1/order

    https://binance-docs.github.io/apidocs/delivery/en/#modify-order-trade

    Args:
        symbol (str)
        side (str)
    Keyword Args:
        orderId (int, optional)
        origClientOrderId (str, optional)
        quantity (float, optional): Order quantity, cannot be sent with closePosition=true
        price (float, optional)
        recvWindow (int, optional)
    Either orderId or origClientOrderId must be sent, and the orderId will prevail if both are sent.
    Either quantity or price must be sent.
    If the modification will cause the order to be cancelled immediately, the modification request will be rejected, in this case the user can force the modification by sending both quantity and price parameters and let the the order be cancelled immediately. So if you want to ensure the success of the modification request, we strongly recommend sending both quantity and price parameters at the same, for example:
    When the new order quantity in the modification request is less than the partially filled quantity, if the user only sends quantity then the modification will fail, if the user sends both quantity and price then the modification will be successful and the order will be cancelled immediately.
    When the new order price in the modification request prevents the GTX order from becoming a pending order (post only), if the user only sends price then the modification will fail, if the user sends both quantity and price then the modification will be successful and the order will be cancelled immediately.
    """
    
    url_path = "/dapi/v1/order"
    params = {}

    if (orderId is None) and (origClientOrderId is None):
        check_required_parameters([[symbol, "symbol"], [side, "side"], [orderId, "orderId"]])
    elif (orderId is None):
        params = {"symbol": symbol, "side": side, "orderId": orderId, **kwargs}
    else:
        params = {"symbol": symbol, "side": side, "origClientOrderId": origClientOrderId, **kwargs}
    
    return self.sign_request("PUT", url_path, params)


def new_batch_order(self, batchOrders:list):
    """Place Multiple Orders (TRADE)

    Post a new batch order

    POST /dapi/v1/batchOrders

    https://binance-docs.github.io/apidocs/delivery/en/#place-multiple-orders-trade

    Paremeter rules are same with New Order
    Batch orders are processed concurrently, and the order of matching is not guaranteed.
    The order of returned contents for batch orders is the same as the order of the order list.
        batchOrders (list): order list. Max 5 orders
    batchOrders is the list of order parameters in JSON：
    Args:
        batchOrders (list)
    Keyword Args:
        recvWindow (int, optional)
    """

    params = {"batchOrders": batchOrders}
    url_path = "/dapi/v1/batchOrders"

    return self.sign_request("POST", url_path, params, True)


def modify_batch_order(self, batchOrders:list):
    """Place Multiple Orders (TRADE)

    Post a new batch order

    PUT /dapi/v1/batchOrders

    https://binance-docs.github.io/apidocs/delivery/en/#modify-multiple-orders-trade

    Paremeter rules are same with New Order
    Batch orders are processed concurrently, and the order of matching is not guaranteed.
    The order of returned contents for batch orders is the same as the order of the order list.
        batchOrders (list): order list. Max 5 orders
    batchOrders is the list of order parameters in JSON：
    Args:
        batchOrders (list)
    Keyword Args:
        recvWindow (int, optional)
    """

    params = {"batchOrders": batchOrders}
    url_path = "/dapi/v1/batchOrders"

    return self.sign_request("PUT", url_path, params)


def order_modify_history(self, symbol: str, orderId: int = None, origClientOrderId: str = None, **kwargs):
    """Get Order Modify History (USER_DATA)

    Get order modification history

    GET /dapi/v1/orderAmendment

    https://binance-docs.github.io/apidocs/delivery/en/#get-order-modify-history-user_data

    Args:
        symbol (str)
    Keyword Args:
        orderId (int, optional)
        origClientOrderId (str, optional)
        startTime (int, optional): Timestamp in ms to get modification history from INCLUSIVE
        endTime (int, optional): Timestamp in ms to get modification history from INCLUSIVE
        limit (int, optional)
        recvWindow (int, optional)
    """
    
    url_path = "/dapi/v1/orderAmendment"
    params = {}

    if (orderId is None) and (origClientOrderId is None):
        check_required_parameters([[symbol, "symbol"], [orderId, "orderId"], ["origClientOrderId", origClientOrderId]])
    elif (orderId is None):
        params = {"symbol": symbol, "orderId": orderId, **kwargs}
    else:
        params = {"symbol": symbol, "origClientOrderId": origClientOrderId, **kwargs}

    return self.sign_request("GET", url_path, params)


def query_order(self, symbol: str, orderId: int = None, origClientOrderId: str = None, **kwargs):
    """Query Order (USER_DATA)

    query a order

    GET /dapi/v1/order

    https://binance-docs.github.io/apidocs/delivery/en/#query-order-user_data

    Args:
        symbol (str)
    Keyword Args:
        orderId (int, optional)
        origClientOrderId (str, optional)
        recvWindow (int, optional)
    """

    url_path = "/dapi/v1/order"
    params = {}

    if (orderId is None) and (origClientOrderId is None):
        check_required_parameters([[symbol, "symbol"], [orderId, "orderId"], ["origClientOrderId", origClientOrderId]])
    elif (orderId is None):
        params = {"symbol": symbol, "orderId": orderId, **kwargs}
    else:
        params = {"symbol": symbol, "origClientOrderId": origClientOrderId, **kwargs}

    return self.sign_request("GET", url_path, params)


def cancel_order(self, symbol: str, orderId: int = None, origClientOrderId: str = None, **kwargs):
    """Cancel Order (TRADE)

    Cancel an active order.

    DELETE /dapi/v1/order

    https://binance-docs.github.io/apidocs/delivery/en/#cancel-order-trade

    Args:
        symbol (str)
    Keyword Args:
        orderId (int, optional)
        origClientOrderId (str, optional)
        newClientOrderId (str, optional)
        recvWindow (int, optional)
    """

    url_path = "/dapi/v1/order"
    params = {}

    if (orderId is None) and (origClientOrderId is None):
        check_required_parameters([[symbol, "symbol"], [orderId, "orderId"], ["origClientOrderId", origClientOrderId]])
    elif (orderId is None):
        params = {"symbol": symbol, "orderId": orderId, **kwargs}
    else:
        params = {"symbol": symbol, "origClientOrderId": origClientOrderId, **kwargs}

    return self.sign_request("DELETE", url_path, params)


def cancel_open_orders(self, symbol: str, **kwargs):
    """Cancel All Open Orders (TRADE)

    /dapi/v1/allOpenOrders

    https://binance-docs.github.io/apidocs/delivery/en/#cancel-all-open-orders-trade

    Args:
        symbol (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/dapi/v1/allOpenOrders"
    params = {"symbol": symbol, **kwargs}
    
    return self.sign_request("DELETE", url_path, params)


def cancel_batch_order(self, symbol: str, orderIdList: list, origClientOrderIdList: list, **kwargs):
    """Cancel Multiple Orders (TRADE)

    Cancel a new batch order

    DELETE /dapi/v1/batchOrders

    https://binance-docs.github.io/apidocs/delivery/en/#cancel-multiple-orders-trade

    Args:
        symbol (str)
        orderIdList (int list): max length 10 e.g. [1234567,2345678]
        origClientOrderIdList (str list): max length 10 e.g. ["my_id_1","my_id_2"], encode the double quotes. No space after comma.
        (Either orderIdList or origClientOrderIdList must be sent.)
    Keyword Args:
        recvWindow (int, optional)
    """
    
    url_path = "/dapi/v1/batchOrders"
    params = {}

    if (orderIdList is None) and (origClientOrderIdList is None):
        check_required_parameters([[symbol, "symbol"], [orderIdList, "orderIdList"], [origClientOrderIdList, "origClientOrderIdList"]])
    elif (orderIdList is None):
        params = {"symbol": symbol, "orderIdList": orderIdList, **kwargs}
    else:
        params = {"symbol": symbol, "origClientOrderIdList": origClientOrderIdList, **kwargs}
    
    return self.sign_request("DELETE", url_path, params)


def countdown_cancel_order(self, symbol: str, countdownTime: int, **kwargs):
    """Auto-Cancel All Open Orders (TRADE)

    Cancel all open orders of the specified symbol at the end of the specified countdown.

    POST /dapi/v1/countdownCancelAll

    https://binance-docs.github.io/apidocs/delivery/en/#auto-cancel-all-open-orders-trade

    Args:
        symbol (str)
        countdownTime (int list): countdown time, 1000 for 1 second. 0 to cancel the timer
    Keyword Args:
        recvWindow (int, optional)

    The endpoint should be called repeatedly as heartbeats so that the existing countdown time can be canceled and replaced by a new one.
    Example usage:
    Call this endpoint at 30s intervals with an countdownTime of 120000 (120s).
    If this endpoint is not called within 120 seconds, all your orders of the specified symbol will be automatically canceled.
    If this endpoint is called with an countdownTime of 0, the countdown timer will be stopped.
    The system will check all countdowns approximately every 10 milliseconds, so please note that sufficient redundancy should be considered when using this function. 
    We do not recommend setting the countdown time to be too precise or too small.
    """
    
    check_required_parameters([[symbol, "symbol"], [countdownTime, "countdownTime"]])
    url_path = "/dapi/v1/countdownCancelAll"
    params = {"symbol": symbol, "countdownTime": countdownTime, **kwargs}

    return self.sign_request("POST", url_path, params)


def get_open_orders(self, symbol: str, orderId: int = None, origClientOrderId: str = None, **kwargs):
    """Query Current Open Order (USER_DATA)

    Get all open orders on a symbol.

    GET /dapi/v1/openOrder

    https://binance-docs.github.io/apidocs/delivery/en/#query-current-open-order-user_data

    Args:
        symbol (str)
        orderId (int, optional)
        origClientOrderId (str, optional)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000

    EitherorderId or origClientOrderId must be sent
    If the queried order has been filled or cancelled, the error message "Order does not exist" will be returned.
    """

    url_path = "/dapi/v1/openOrder"
    params = {}

    if (orderId is None) and (origClientOrderId is None):
        check_required_parameters([[symbol, "symbol"], [orderId, "orderId"], [origClientOrderId, "origClientOrderId"]])
    elif (orderId is None):
        params = {"symbol": symbol, "orderId": orderId, **kwargs}
    else:
        params = {"symbol": symbol, "origClientOrderId": origClientOrderId, **kwargs}
    
    return self.sign_request("GET", url_path, params)


def get_orders(self, **kwargs):
    """Current All Open Orders (USER_DATA)

    Get all open orders on a symbol. Careful when accessing this with no symbol.
    If the symbol is not sent, orders for all symbols will be returned in an array.

    GET /dapi/v1/openOrders

    https://binance-docs.github.io/apidocs/delivery/en/#current-all-open-orders-user_data

    Args:
    Keyword Args:
        symbol (str, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/dapi/v1/openOrders"
    params = { **kwargs }

    return self.sign_request("GET", url_path, params)


def get_all_orders(self, **kwargs):
    """All Orders (USER_DATA)

    Get all account orders; active, canceled, or filled.

    GET /dapi/v1/allOrders

    https://binance-docs.github.io/apidocs/delivery/en/#all-orders-user_data

    Args:
    Keyword Args:
        symbol (str)
        orderId (int, optional)
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): Default 50; max 100.
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/dapi/v1/allOrders"
    params = {**kwargs}

    return self.sign_request("GET", url_path, params)


def balance(self, **kwargs):
    """Futures Account Balance (USER_DATA)

    Get current account balance

    GET /dapi/v1/balance

    https://binance-docs.github.io/apidocs/delivery/en/#futures-account-balance-user_data

    Keyword Args:
        recvWindow (int, optional)
    """

    url_path = "/dapi/v1/balance"
    return self.sign_request("GET", url_path, {**kwargs})


def account(self, **kwargs):
    """Account Information (USER_DATA)

    Get current account information

    GET /dapi/v1/account

    https://binance-docs.github.io/apidocs/delivery/en/#account-information-user_data

    Keyword Args:
        recvWindow (int, optional)
    for One-way Mode user, the "positions" will only show the "BOTH" positions
    for Hedge Mode user, the "positions" will show "BOTH", "LONG", and "SHORT" positions.
    """

    url_path = "/dapi/v1/account"
    return self.sign_request("GET", url_path, {**kwargs})


def change_leverage(self, symbol: str, leverage: int, **kwargs):
    """Change Initial Leverage (TRADE)

    Change user's initial leverage in the specific symbol market.
    For Hedge Mode, LONG and SHORT positions of one symbol use the same initial leverage and share a total notional value.

    POST /dapi/v1/leverage

    https://binance-docs.github.io/apidocs/delivery/en/#change-initial-leverage-trade

    Args:
        symbol (str)
        leverage (int): target initial leverage: int from 1 to 125
    Keyword Args:
        recvWindow (int, optional)
    """

    check_required_parameters([[symbol, "symbol"],[leverage, "leverage"]])

    url_path = "/dapi/v1/leverage"
    params = {"symbol": symbol, "leverage":leverage, **kwargs}
    return self.sign_request("POST", url_path, params)


def change_margin_type(self, symbol: str, marginType: str, **kwargs):
    """Change margin type(TRADE)

    Change user's margin type in the specific symbol market.For Hedge Mode, LONG and SHORT positions of one symbol use the same margin type.
    With ISOLATED margin type, margins of the LONG and SHORT positions are isolated from each other.

    POST /dapi/v1/marginType

    https://binance-docs.github.io/apidocs/delivery/en/#change-margin-type-trade

    Args:
        symbol (str)
        marginType (str): ISOLATED, CROSSED
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[symbol, "symbol"],[marginType, "marginType"]])

    url_path = "/dapi/v1/marginType"
    params = {"symbol": symbol, "marginType":marginType, **kwargs}
    return self.sign_request("POST", url_path, params)


def modify_isolated_position_margin(self, symbol: str, amount: float, type: int, **kwargs):
    """Modify Isolated Position Margin (TRADE)

    POST /dapi/v1/positionMargin

    https://binance-docs.github.io/apidocs/delivery/en/#modify-isolated-position-margin-trade

    Args:
        symbol (str)
        amount (float)
        type (int): 1: Add position margin，2: Reduce position margin
    Keyword Args:
        positionSide (str, optional): Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent with Hedge Mode.
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[symbol, "symbol"],[amount, "amount"], [type, "type"]])

    url_path = "/dapi/v1/positionMargin"
    params = {"symbol": symbol, "amount":amount, "type":type, **kwargs}
    return self.sign_request("POST", url_path, params)


def get_position_margin_history(self, symbol: str, **kwargs):
    """Get Position Margin Change History (TRADE)

    Get position margin history on a symbol.

    GET /dapi/v1/positionMargin/history

    https://binance-docs.github.io/apidocs/delivery/en/#get-position-margin-change-history-trade

    Args:
        symbol (str, optional)
    Keyword Args:
        type (int, optional): 1: Add position margin，2: Reduce position margin
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): default: 50
        recvWindow (int, optional)
    """

    check_required_parameter(symbol, "symbol")
    url_path = "/dapi/v1/positionMargin/history"
    params = {"symbol": symbol, **kwargs}

    return self.sign_request("GET", url_path, params)


def get_position_risk(self, **kwargs):
    """Position Information (USER_DATA)

    Get current position information.

    GET /dapi/v1/positionRisk

    https://binance-docs.github.io/apidocs/delivery/en/#position-information-user_data

    Args:
        symbol (str, optional)
    Keyword Args:
        recvWindow (int, optional)

    """

    url_path = "/dapi/v1/positionRisk"
    params = {**kwargs}

    return self.sign_request("GET", url_path, params)


def get_account_trades(self, **kwargs):
    """Account Trade List (USER_DATA)

    Get trades for a specific account and symbol.

    GET /dapi/v1/userTrades

    https://binance-docs.github.io/apidocs/delivery/en/#account-trade-list-user_data

    Args:
        
    Keyword Args:
        symbol (str, optional)
        pair (str, optional)
        startTime (int, optional)
        endTime (int, optional)
        fromId (int, optional): Trade id to fetch from. Default gets most recent trades.
        limit (int, optional): Default 50; max 100.
        recvWindow (int, optional)

    Either symbol or pair must be sent
    Symbol and pair cannot be sent together
    Pair and fromId cannot be sent together
    If a pair is sent,tickers for all symbols of the pair will be returned
    The parameter fromId cannot be sent with startTime or endTime
    """

    url_path = "/dapi/v1/userTrades"
    params = {**kwargs}

    return self.sign_request("GET", url_path, params)


def get_income_history(self, **kwargs):
    """Get Income History(USER_DATA)

    Get trades for a specific account and symbol.

    GET /dapi/v1/income

    https://binance-docs.github.io/apidocs/delivery/en/#get-income-history-user_data

    Args:
    Keyword Args:
        symbol (str, optional)
        incomeType (str, optional): "TRANSFER"，"WELCOME_BONUS", "REALIZED_PNL"，"FUNDING_FEE", "COMMISSION" and "INSURANCE_CLEAR"
        startTime (int, optional): Timestamp in ms to get funding from INCLUSIVE.
        endTime (int, optional): Timestamp in ms to get funding from INCLUSIVE.
        limit (int, optional): Default 100; max 1000
        recvWindow (int, optional)

    If incomeType is not sent, all kinds of flow will be returned
    "trandId" is unique in the same incomeType for a user
    """

    url_path = "/dapi/v1/income"
    params = {**kwargs}

    return self.sign_request("GET", url_path, params)


def leverage_brackets(self, symbol: str = None, pair: str = None, **kwargs):
    """Notional and Leverage Brackets (USER_DATA)

    Get notional and leverage bracket.

    GET /dapi/v1/leverageBracket
    GET /dapi/v2/leverageBracket

    https://binance-docs.github.io/apidocs/delivery/en/#notional-bracket-for-pair-user_data
    https://binance-docs.github.io/apidocs/delivery/en/#notional-bracket-for-pair-user_data-2

    Args:
    Keyword Args:
        symbol (str, optional)
        pair (str, optional)
        recvWindow (int, optional)
    """

    url_path = ""
    params = {}

    if (symbol is None) and (pair is None):
        url_path = "/dapi/v2/leverageBracket"
        params = {**kwargs}
    elif (symbol is None):
        url_path = "/dapi/v2/leverageBracket"
        params = {"symbol": symbol, **kwargs}
    else:
        url_path = "/dapi/v1/leverageBracket"
        params = {"pair": pair,  **kwargs}

    return self.sign_request("GET", url_path, params)


def adl_quantile(self, **kwargs):
    """Position ADL Quantile Estimation(USER_DATA)

    Get Position ADL Quantile Estimation

    GET /dapi/v1/adlQuantile

    https://binance-docs.github.io/apidocs/delivery/en/#position-adl-quantile-estimation-user_data

    Args:
    Keyword Args:
        symbol (str, optional)
        recvWindow (int, optional)

    Values update every 30s.
    Values 0, 1, 2, 3, 4 shows the queue position and possibility of ADL from low to high.
    For positions of the symbol are in One-way Mode or isolated margined in Hedge Mode, "LONG", "SHORT", and "BOTH" will be returned to show the positions' adl quantiles of different position sides.

    If the positions of the symbol are crossed margined in Hedge Mode:
    "HEDGE" as a sign will be returned instead of "BOTH";
    A same value caculated on unrealized pnls on long and short sides' positions will be shown for "LONG" and "SHORT" when there are positions in both of long and short sides.
    """

    url_path = "/dapi/v1/adlQuantile"
    params = {**kwargs}

    return self.sign_request("GET", url_path, params)


def force_orders(self, **kwargs):
    """User's Force Orders (USER_DATA)

    Get User's Force Orders

    GET /dapi/v1/forceOrders

    https://binance-docs.github.io/apidocs/delivery/en/#user-39-s-force-orders-user_data

    Args:
    Keyword Args:
        symbol (str, optional)
        autoCloseType (str, optional): "LIQUIDATION" for liquidation orders, "ADL" for ADL orders.
        startTime (int, optional): Start Time.
        endTime (int, optional): End Time.
        Limit (int, optional): Default 50; max 100.
        recvWindow (int, optional)

    If "autoCloseType" is not sent, orders with both of the types will be returned
    If "startTime" is not sent, data within 200 days before "endTime" can be queried
    """

    url_path = "/dapi/v1/forceOrders"
    params = {**kwargs}

    return self.sign_request("GET", url_path, params)


def commission_rate(self, symbol: str, **kwargs):
    """User Commission Rate (USER_DATA)

    Get commission rate of symbol

    GET /dapi/v1/commissionRate

    https://binance-docs.github.io/apidocs/delivery/en/#user-commission-rate-user_data

    Args:
        symbol (str, optional)
    Keyword Args:
        recvWindow (int, optional)
    """
    
    check_required_parameter(symbol, "symbol")
    url_path = "/dapi/v1/commissionRate"
    params = {"symbol":symbol, **kwargs}

    return self.sign_request("GET", url_path, params)
