# aiogram cache

[![PyPi Package Version](https://img.shields.io/pypi/v/aiogram_cache.svg?style=flat-square)](https://pypi.python.org/pypi/aiogram_cache)
[![PyPi status](https://img.shields.io/pypi/status/aiogram_cache.svg?style=flat-square)](https://pypi.python.org/pypi/aiogram_cache)
[![Downloads](https://pepy.tech/badge/aiogram_cache)](https://pepy.tech/project/aiogram_cache)
[![Supported python versions](https://img.shields.io/pypi/pyversions/aiogram_cache.svg?style=flat-square)](https://pypi.python.org/pypi/aiogram_cache)
[![repository size](https://img.shields.io/github/repo-size/alteralt/aiogram_cache)](https://github.com/alteralt/aiogram_cache)

# Install
``pip install aiogram_cache``

# How to use

```python
import aiohttp
import aiogram_cache
from aiogram import Bot, Dispatcher, types, executor
# Импортируем объект хранилища в памяти
from aiogram_cache.storages.memory import MemoryStorage as CacheMemoryStorage


BOT_TOKEN = ""


bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

cache_storage = CacheMemoryStorage()  # Инициализируем хранилище
dp.middleware.setup(aiogram_cache.CacheMiddleware(cache_storage))  # Подключаем мидлварь


async def get_usd_price() -> float:
    """
    Функция для получения цены доллара по отношению к рублю
    """
    async with aiohttp.ClientSession() as session:
        async with await session.get("https://www.cbr-xml-daily.ru/daily_json.js") as response:
            json_response = await response.json(content_type=None)
            return round(float(json_response["Valute"]["USD"]["Value"]), 2)

        
@dp.message_handler(commands=["price"])
async def price(message: types.Message, cache: aiogram_cache.CacheContext):
    # Получаем данные из кеша по ключу
    usd_price = await cache.get("price")
    if usd_price is None:
        # Если значения в кеше нет, или оно устарело
        # Получаем актуальное значение
        usd_price = await get_usd_price()
        
        # И записываем его в кеш на 30 секунд
        await cache.set("price", usd_price, timeout=30)
        
    await message.answer("Стоимость доллара к рублю: {}".format(usd_price))


if __name__ == '__main__':
    executor.start_polling(dp)
```
