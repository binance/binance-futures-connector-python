from binance.lib.utils import check_required_parameter


def new_listen_key(self):
    """
    |
    | **Create a ListenKey (USER_STREAM)**

    :API endpoint: ``POST /dapi/v1/listenKey``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/user-data-streams/Start-User-Data-Stream
    |
    """

    url_path = "/dapi/v1/listenKey"
    return self.send_request("POST", url_path)


def renew_listen_key(self, listenKey: str):
    """
    | **Ping/Keep-alive a ListenKey (USER_STREAM)**

    :API endpoint: ``PUT /dapi/v1/listenKey``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/user-data-streams/Keepalive-User-Data-Stream

    :parameter listenKey: string
    |
    """

    check_required_parameter(listenKey, "listenKey")
    url_path = "/dapi/v1/listenKey"
    return self.send_request("PUT", url_path, {"listenKey": listenKey})


def close_listen_key(self, listenKey: str):
    """
    |
    | **Close a ListenKey (USER_STREAM)**

    :API endpoint: ``DELETE /dapi/v1/listenKey``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/user-data-streams/Close-User-Data-Stream

    :parameter listenKey: string
    |
    """

    check_required_parameter(listenKey, "listenKey")
    url_path = "/dapi/v1/listenKey"
    return self.send_request("DELETE", url_path, {"listenKey": listenKey})
