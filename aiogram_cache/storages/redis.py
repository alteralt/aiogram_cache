import typing
import asyncio
import aioredis

from aiogram_cache.storage import BaseStorage


class RedisStorage(BaseStorage):
    def __init__(
            self,
            host: str = "localhost",
            port: int = 6379,
            db: typing.Optional[int] = None,
            password: typing.Optional[str] = None,
            ssl: typing.Optional[bool] = None,
            pool_size: int = 10,
            prefix: str = "aiogram_cache",
            redis_pool: typing.Optional[aioredis.Redis] = None
    ):
        self._host = host
        self._port = port
        self._db = db
        self._password = password
        self._ssl = ssl
        self._pool_size = pool_size
        self._prefix = (prefix,)

        self._redis: typing.Optional[aioredis.Redis] = redis_pool
        self._connection_lock = asyncio.Lock()

    async def _get_redis(self) -> aioredis.Redis:
        if self._redis is None:
            async with self._connection_lock:
                if self._redis is None:
                    self._redis = aioredis.Redis(
                        host=self._host,
                        port=self._port,
                        db=self._db,
                        password=self._password,
                        ssl=self._ssl,
                        max_connections=self._pool_size,
                        decode_responses=True,
                    )

        return self._redis

    async def close(self):
        if self._redis:
            await self._redis.close()

    def generate_key(self, *parts):
        return ":".join(self._prefix + tuple(map(str, parts)))

    async def get(self, key):
        redis = await self._get_redis()
        return await redis.get(self.generate_key(key))

    async def set(self, key, value, timeout=-1):
        redis = await self._get_redis()
        await redis.set(self.generate_key(key), value, ex=timeout)

    async def delete(self, key):
        redis = await self._get_redis()
        await redis.delete(key)
