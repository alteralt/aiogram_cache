from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware

from aiogram_cache.storage import CacheContext, BaseStorage


class CacheMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update"]

    def __init__(self, cache_storage: BaseStorage):
        super().__init__()

        self.cache_storage = cache_storage

    async def pre_process(self, obj, data, *args):
        data["cache"] = CacheContext(self.cache_storage)
