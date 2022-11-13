import time

from aiogram_cache.storage import BaseStorage


class MemoryStorage(BaseStorage):
    def __init__(self):
        self.data = {}

    async def close(self):
        pass

    @classmethod
    def generate_key(cls, *parts):
        return ':'.join(tuple(map(str, parts)))

    async def get(self, key):
        record = self.data.get(self.generate_key(key), {"expiry_on": 0, "value": None})
        return record["value"] if time.time() < record["expiry_on"] else None

    async def set(self, key, value, timeout=-1):
        self.data[self.generate_key(key)] = {
            "value": value,
            "expiry_on": time.time() + timeout
        }

    async def delete(self, key):
        if key in self.data:
            del self.data[key]
