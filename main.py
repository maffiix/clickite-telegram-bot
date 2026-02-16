from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import os
from dotenv import load_dotenv
import asyncio
import logging

from handlers import greeting

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2)
)
dispatcher = Dispatcher()

dispatcher.include_router(greeting.router)


async def on_startup():
    logging.info('🔃 All routers included!')
    logging.info('🚀 Bot started! Access it via Telegram!')


async def main():
    await on_startup()
    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())