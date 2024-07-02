import asyncio
import os
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.files import JSONStorage
from telegram.services import TGBot

bot = Bot(
    token=TGBot.get_bot_token(bot_name="Бот для отчетов"),
    proxy="http://172.16.1.253:3128",
    parse_mode="HTML",
)
storage = JSONStorage(f'{Path.cwd()}/{"fsm_data.json"}')
loop = asyncio.get_event_loop()
dp = Dispatcher(bot, storage=storage, loop=loop)


if __name__ == "__main__":
    storage.write(Path.cwd())
