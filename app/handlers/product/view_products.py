from aiogram import Router, types
from aiogram.filters import Command
from app.services.product_service import get_products

router = Router()

@router.message(Command("products"))
async def products_handler(message: types.Message):
    products = await get_products()

    if not products:
        await message.answer("Нет доступных товаров")
        return

    text = "Список товаров:\n\n"
    for product in products:
        text += (
            f"{product['name']}\n"
            f"Цена: {product['price']} руб.\n"
            f"Категория: {product['category']}\n\n"
        )

    await message.answer(text)