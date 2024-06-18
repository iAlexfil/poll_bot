import sys
from os import getenv
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import bot.admin.commands
from bot.handlers.commands import register_handlers


TOKEN = getenv('TOKEN')

dp = Dispatcher(storage=MemoryStorage())

bot.admin.commands.register_handlers(dp)
bot.handlers.commands.register_handlers(dp)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.delete_webhook()

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
