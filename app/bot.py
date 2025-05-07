import asyncio
from aiogram import Bot, Dispatcher
from app.config import BOT_TOKEN
from app.handlers.user import register, profile
from app.handlers.product import view_products, get_product
from app.handlers.cart import add_to_cart

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(register.router)
    dp.include_router(profile.router)
    dp.include_router(view_products.router)
    dp.include_router(get_product.router)
    dp.include_router(add_to_cart.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
