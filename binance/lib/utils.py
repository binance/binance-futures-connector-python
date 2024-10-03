import json
import time

from urllib.parse import urlencode, urlparse
from binance.error import (
    ParameterRequiredError,
    ParameterValueError,
    ParameterTypeError,
)


def cleanNoneValue(d) -> dict:
    out = {}
    for k in d.keys():
        if d[k] is not None:
            out[k] = d[k]
    return out


def check_required_parameter(value, name):
    if not value and value != 0:
        raise ParameterRequiredError([name])


def check_required_parameters(params):
    """validate multiple parameters
    params = [
        ['btcusdt', 'symbol'],
        [10, 'price']
    ]

    """
    for p in params:
        check_required_parameter(p[0], p[1])


def check_enum_parameter(value, enum_class):
    if value not in set(item.value for item in enum_class):
        raise ParameterValueError([value])


def check_type_parameter(value, name, data_type):
    if value is not None and not isinstance(value, data_type):
        raise ParameterTypeError([name, data_type])


def get_timestamp():
    return int(time.time() * 1000)


def encoded_string(query, special=False):
    if special:
        return urlencode(query).replace("%40", "@").replace("%27", "%22")
    else:
        return urlencode(query, True).replace("%40", "@")


def convert_list_to_json_array(symbols):
    if symbols is None:
        return symbols
    res = json.dumps(symbols)
    return res.replace(" ", "")


def config_logging(logging, logging_devel, log_file=None):
    logging.basicConfig(level=logging_devel, filename=log_file)


def parse_proxies(proxies: dict):
    """Parse proxy url from dict, only support http and https proxy, not support socks5 proxy"""
    proxy_url = proxies.get("http") or proxies.get("https")
    if not proxy_url:
        return {}

    parsed = urlparse(proxy_url)
    return {
        "http_proxy_host": parsed.hostname,
        "http_proxy_port": parsed.port,
        "http_proxy_auth": (
            (parsed.username, parsed.password)
            if parsed.username and parsed.password
            else None
        ),
    }
