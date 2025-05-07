from aiogram import Router, types
from aiogram.filters import Command

from app.services.cart_service import get_cart

router = Router()

@router.message(Command("cart"))
async def view_cart_handler(message: types.Message):
    user_id = message.from_user.id
    items = await get_cart(user_id)

    if not items:
        await message.answer("Ваша корзина пуста")
        return

    text = "Ваша корзина:\n\n"
    total = 0

    for item in items:
        text += (
            f"{item['name']} — {item['quantity']} шт. × {item['price']} руб. = {item['total_price']} руб.\n"
        )
        total += item["total_price"]

    text += f"\nИтиго: {total} руб."
    await message.answer(text)