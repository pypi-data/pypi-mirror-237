import psutil

from .base import BaseCollection
from .enums import MetricsEnum
from .utils import get_human_readable_size


class MemoryCollector(BaseCollection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def event_type(self):
        return MetricsEnum.disk.value

    @property
    def memory(self):
        return psutil.virtual_memory()

    @property
    def available(self):
        return get_human_readable_size(self.memory.available)

    @property
    def total(self):
        return get_human_readable_size(self.memory.total)

    @property
    def percentage(self):
        return self.memory.percent

    @property
    def used(self):
        return get_human_readable_size(self.memory.used)

    @property
    def free(self):
        return get_human_readable_size(self.memory.free)

    @property
    def active(self):
        return get_human_readable_size(self.memory.active)

    @property
    def inactive(self):
        return get_human_readable_size(self.memory.inactive)

    def to_dict(self):
        return {
            "headers": {
                "hostname": self.hostname,
                "ipaddress": self.ipaddress,
                "event_timestamp": self.event_timestamp,
                "event_type": self.event_type
            },
            "payload": {
                "available": self.available,
                "free": self.free,
                "used": self.used,
                "active": self.active,
                "inactive": self.inactive,
            }
        }
