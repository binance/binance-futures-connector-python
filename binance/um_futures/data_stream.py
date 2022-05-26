from binance.lib.utils import check_required_parameter


def new_listen_key(self):
    """
    |
    | **Create a ListenKey (USER_STREAM)**

    :API endpoint: ``POST /fapi/v1/listenKey``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#start-user-data-stream-user_stream
    |
    """

    url_path = "/fapi/v1/listenKey"
    return self.send_request("POST", url_path)


def renew_listen_key(self, listenKey: str):
    """
    |
    | **Ping/Keep-alive a ListenKey (USER_STREAM)**

    :API endpoint: ``PUT /fapi/v1/listenKey``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#keepalive-user-data-stream-user_stream

    :parameter listenKey: string
    |
    """

    check_required_parameter(listenKey, "listenKey")
    url_path = "/fapi/v1/listenKey"
    return self.send_request("PUT", url_path, {"listenKey": listenKey})


def close_listen_key(self, listenKey: str):
    """
    |
    | **Close a ListenKey (USER_STREAM)**

    :API endpoint: ``DELETE /fapi/v1/listenKey``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#close-user-data-stream-user_stream

    :parameter listenKey: string
    |
    """

    check_required_parameter(listenKey, "listenKey")
    url_path = "/fapi/v1/listenKey"
    return self.send_request("DELETE", url_path, {"listenKey": listenKey})
