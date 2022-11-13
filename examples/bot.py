import aiogram_cache
from aiogram import Bot, Dispatcher, types, executor
from aiogram_cache.storages.memory import MemoryStorage as CacheMemoryStorage


BOT_TOKEN = ""


bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

cache_storage = CacheMemoryStorage()
dp.middleware.setup(aiogram_cache.CacheMiddleware(cache_storage))


@dp.message_handler(commands=["set"])
async def set_cache(message: types.Message, cache: aiogram_cache.CacheContext):
    command, key, value = message.text.split(" ")
    await cache.set(key, value, timeout=60)
    await message.answer("Установлено новое значение для ключа {}".format(key))


@dp.message_handler(commands=["get"])
async def get_cache(message: types.Message, cache: aiogram_cache.CacheContext):
    command, key = message.text.split(" ")
    value = await cache.get(key)
    await message.answer("Получено значение: {}".format(value))


if __name__ == '__main__':
    executor.start_polling(dp)
