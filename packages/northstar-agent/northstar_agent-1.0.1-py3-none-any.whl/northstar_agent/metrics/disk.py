import psutil

from .base import BaseCollection
from .utils import get_human_readable_size


class Partition:
    def __init__(self, device, mountpoint):
        self.device = device
        self.mountpoint = mountpoint

    @property
    def total(self):
        return get_human_readable_size(psutil.disk_usage(self.mountpoint).total)

    @property
    def used(self):
        return get_human_readable_size(psutil.disk_usage(self.mountpoint).used)

    @property
    def free(self):
        return get_human_readable_size(psutil.disk_usage(self.mountpoint).free)

    @property
    def percentage(self):
        return get_human_readable_size(psutil.disk_usage(self.mountpoint).percent)

    def to_dict(self):
        return {
            "device": self.device,
            "mountpoint": self.mountpoint,
            "total": self.total,
            "used": self.used,
            "free": self.free,
            "percentage": self.percentage,
        }


class DiskCollector(BaseCollection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def to_dict():
        return [
            Partition(device=partition.device, mountpoint=partition.mountpoint).to_dict()
            for partition in psutil.disk_partitions()
        ]
