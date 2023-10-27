from datetime import datetime
import socket
import requests


class BaseCollection:
    def __init__(self, *args, **kwargs):
        pass

    @property
    def event_type(self):
        raise NotImplementedError

    @property
    def hostname(self):
        """Return host name"""
        return socket.gethostname()

    @property
    def ipaddress(self):
        """Property to retrieve the public IP address of the host"""
        return requests.get("https://api.ipify.org").content.decode("utf8")

    @property
    def event_timestamp(self):
        return datetime.utcnow().isoformat()
