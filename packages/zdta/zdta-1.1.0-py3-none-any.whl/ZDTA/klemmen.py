"""
Module klemmen.py to do klemmen 15 and 30 control.
Include with these SDK:
    start_kl_30: start klemmen 30 gpio.
    stop_kl_30: stop klemmen 30 gpio.
    get_kl_30_status: get klemmen 30 gpio status.
    start_kl_15: start klemmen 30 gpio.
    stop_kl_15: stop klemmen 30 gpio.
    get_kl_15_status: get klemmen 30 gpio status.
"""

from __common import render_result, send_request
from __service_config import SERVER_PORT, DEFAULT

# constant
BASE_KLEMMEN_PORT = SERVER_PORT["KL_URL"]


class Klemmen:
    """Class Klemmen instance."""

    def __init__(self, did, device):
        """Function init"""
        self.did = did
        self.device = device
        self.event = "kl_event"

    def get_ip(self):
        """Function get server ip"""
        return f"http://{DEFAULT['ip_address']}:{BASE_KLEMMEN_PORT}"

    @render_result
    def start_kl_30(self):
        """Function start klemmen 30."""
        # request middle service
        url = f"{self.get_ip()}/30"
        ret = send_request(
            method="post",
            url=url,
        )
        return ret

    @render_result
    def stop_kl_30(self):
        """Function stop klemmen 30."""
        # request middle service
        url = f"{self.get_ip()}/30"
        ret = send_request(
            method="delete",
            url=url,
        )
        return ret

    @render_result
    def get_kl_30_status(self):
        """Function get klemmen 30 status."""
        # request middle service
        url = f"{self.get_ip()}/30"
        ret = send_request(
            method="get",
            url=url,
        )
        return ret

    @render_result
    def start_kl_15(self, port_id):
        """Function start klemmen 15."""
        # request middle service
        url = f"{self.get_ip()}/15"
        json = {"port_id": port_id}
        ret = send_request(
            method="post",
            json=json,
            url=url,
        )
        return ret

    @render_result
    def stop_kl_15(self):
        """Function stop klemmen 15."""
        # request middle service
        url = f"{self.get_ip()}/15"
        ret = send_request(
            method="delete",
            url=url,
        )
        return ret

    @render_result
    def get_kl_15_status(self):
        """Function get klemmen 15 status."""
        # request middle service
        url = f"{self.get_ip()}/15"
        ret = send_request(
            method="get",
            url=url,
        )
        return ret
