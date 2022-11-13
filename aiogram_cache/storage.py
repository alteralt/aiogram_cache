class BaseStorage:
    async def close(self):
        raise NotImplementedError

    async def get(self, key):
        raise NotImplementedError

    async def set(self, key, value, timeout=-1):
        raise NotImplementedError

    async def delete(self, key):
        raise NotImplementedError


class CacheContext:
    def __init__(self, storage: BaseStorage):
        self.storage: BaseStorage = storage

    async def get(self, key):
        return await self.storage.get(key)

    async def set(self, key, value, timeout=-1):
        await self.storage.set(key, value, timeout=timeout)

    async def delete(self, key):
        await self.storage.delete(key)
