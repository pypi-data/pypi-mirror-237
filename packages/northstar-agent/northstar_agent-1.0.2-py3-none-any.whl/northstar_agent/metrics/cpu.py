import psutil

from .base import BaseCollection
from .enums import MetricsEnum


class CpuCollector(BaseCollection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def event_type(self):
        return MetricsEnum.cpu.value

    @property
    def core_count(self):
        """Return the number of physical cores

        Returns:
            int: Total number of physical CPU cores
        """
        return psutil.cpu_count()

    @property
    def load_avg(self):
        """Return the average system load over the last 1, 5 and 15 minutes as a tuple.

        Returns:
            tuple: Average system load over the last 1, 5 and 15 minutes
        """
        return psutil.getloadavg()

    def to_dict(self):
        return {
            "headers": {
                "hostname": self.hostname,
                "ipaddress": self.ipaddress,
                "event_timestamp": self.event_timestamp,
                "event_type": self.event_type
            },
            "payload": {"cores": self.core_count, "load_avg": self.load_avg}
        }
