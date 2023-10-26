import psutil

from .base import BaseCollection
from .utils import get_human_readable_size


class MemoryCollector(BaseCollection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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

    @property
    def cached(self):
        return get_human_readable_size(self.memory.cached)

    def to_dict(self):
        return {
            "available": self.available,
            "free": self.free,
            "used": self.used,
            "active": self.active,
            "inactive": self.inactive,
            # "cached": self.cached
        }
