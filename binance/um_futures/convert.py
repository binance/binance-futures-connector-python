from binance.lib.utils import check_required_parameter


def list_all_convert_pairs(self, **kwargs):
    """
    |
    | **List All Convert Pairs**
    | *User needs to supply either or both of the input parameter*
    | *If not defined for both fromAsset and toAsset, only partial token pairs will be returned*
    | *Asset BNFCR is only available to convert for MICA region users.*

    :API endpoint: ``GET /fapi/v1/convert/exchangeInfo``
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/convert

    :parameter fromAsset: optional string; EITHER OR BOTH - User spends coin
    :parameter toAsset: optional string; EITHER OR BOTH - User receives coin
    |
    """

    url_path = "/fapi/v1/convert/exchangeInfo"
    params = {**kwargs}

    return self.sign_request("GET", url_path, params)


def send_quote_request(self, fromAsset: str, toAsset: str, **kwargs):
    """
    |
    | **Send Quote Request(USER_DATA)**
    | *Either fromAmount or toAmount should be sent*
    | *quoteId will be returned only if you have enough funds to convert*

    :API endpoint: ``POST /fapi/v1/convert/getQuote``
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/convert/Send-quote-request

    :parameter fromAsset: string; the asset to convert from
    :parameter toAsset: string; the asset to convert to
    :parameter fromAmount: optional float; When specified, it is the amount you will be debited after the conversion
    :parameter toAmount: optional float; When specified, it is the amount you will be credited after the conversion
    :parameter validTime: optional string; 10s, default 10s
    :parameter recvWindow: optional int
    |
    """

    check_required_parameter(fromAsset, "fromAsset")
    check_required_parameter(toAsset, "toAsset")
    url_path = "/fapi/v1/convert/getQuote"
    params = {"fromAsset": fromAsset, "toAsset": toAsset, **kwargs}

    return self.sign_request("POST", url_path, params)


def accept_offered_quote(self, quoteId: str, **kwargs):
    """
    |
    | **Accept the offered quote (USER_DATA)**

    :API endpoint: ``POST /fapi/v1/convert/acceptQuote``
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/convert/Accept-Quote

    :parameter quoteId: string
    :parameter recvWindow: optional int
    |
    """

    check_required_parameter(quoteId, "quoteId")
    url_path = "/fapi/v1/convert/acceptQuote"
    params = {"quoteId": quoteId, **kwargs}

    return self.sign_request("POST", url_path, params)


def order_status(self, **kwargs):
    """
    |
    | **Order status(USER_DATA)**

    :API endpoint: ``GET /fapi/v1/convert/orderStatus``
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/convert/Order-Status

    :parameter orderId: optional string; Either orderId or quoteId is required
    :parameter quoteId: optional string; Either orderId or quoteId is required
    |
    """

    url_path = "/fapi/v1/convert/orderStatus"
    params = {**kwargs}

    return self.sign_request("GET", url_path, params)
