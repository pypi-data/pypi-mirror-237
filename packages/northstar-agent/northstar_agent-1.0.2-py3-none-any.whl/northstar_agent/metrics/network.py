import psutil

from .base import BaseCollection
from .enums import MetricsEnum


class NetworkCollector(BaseCollection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def event_type(self):
        return MetricsEnum.disk.value

    @property
    def io_counters(self):
        return psutil.net_io_counters()

    @property
    def bytes_sent(self):
        return self.io_counters.bytes_sent

    @property
    def bytes_recv(self):
        return self.io_counters.bytes_recv

    @property
    def packets_sent(self):
        return self.io_counters.packets_sent

    @property
    def packets_recv(self):
        return self.io_counters.packets_recv

    def to_dict(self):
        return {
            "headers": {
                "hostname": self.hostname,
                "ipaddress": self.ipaddress,
                "event_timestamp": self.event_timestamp,
                "event_type": self.event_type
            },
            "payload": {
                "bytes_sent": self.bytes_sent,
                "bytes_recv": self.bytes_recv,
                "packets_sent": self.packets_sent,
                "packets_recv": self.packets_recv,
            }
        }
