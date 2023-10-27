"""
Module __common.py with some common def.
"""

import traceback
from functools import wraps
from requests import request, exceptions

import __service_config


def set_config(config):
    """Set Config first to connect server."""
    if "ip_address" in config and config["ip_address"]:
        __service_config.DEFAULT["ip_address"] = config["ip_address"]


def send_request(method="get", url="", timeout=5, **kargs):
    """Function send request with same code."""
    try:
        print("url --------------", url)
        ret = request(method=method, url=url, timeout=timeout, **kargs)
        status_code = ret.status_code

        data = None
        error_message = None
        # request success, get data to return

        if status_code == 200:
            result = ret.json()
            print("result ----------", result)
            data = result.get("data")
            return {"result": data, "error": ""}
        elif status_code != 500:
            # request error, return error message
            result = ret.json()
            error_message = result.get("message")
        else:
            error_message = ret.text or "request middle service error"
        return {"result": False, "error": error_message}
    except exceptions.RequestException as e:
        print(e)
        return {
            "result": False,
            "error": str(traceback.format_exc()),
        }


def render_result(func):
    """Function render the same result style."""

    @wraps(func)
    def decorated(self, *args, **kwargs):
        ret = func(self, *args, **kwargs)
        result = ret["result"]
        return result

    return decorated
