from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware

from aiogram_cache.storage import CacheContext


class CacheMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update"]

    async def pre_process(self, obj, data, *args):
        data["cache_manager"] = CacheContext(self.manager.dispatcher["cache_storage"])
