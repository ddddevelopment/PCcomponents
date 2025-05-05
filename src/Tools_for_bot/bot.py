import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from src.Configs.templates import hello_message, help_message

logging.basicConfig(level=logging.INFO)

API_TOKEN = '7518012877:AAETe5fbbD4PraytXhKn6nUrkQRz3Xfoh6Q'  # Замени на свой токен
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.reply(hello_message)


@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.reply(help_message)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())