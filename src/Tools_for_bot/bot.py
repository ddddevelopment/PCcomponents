import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.Tools_for_bot.config import config
from src.Tools_for_bot.handlers import common, registration
from src.Tools_for_bot.services.users_service import users_service


async def main() -> None:
    storage = MemoryStorage()
    
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher(storage=storage)
    
    dp.include_router(common.router)
    dp.include_router(registration.router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())