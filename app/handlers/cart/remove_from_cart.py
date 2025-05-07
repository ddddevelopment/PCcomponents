from aiogram import Router, types
from aiogram.filters import Command, CommandObject

from app.services.product_service import get_product
from app.services.cart_service import remove_from_cart

router = Router()

@router.message(Command("remove_from_cart"))
async def remove_from_cart_handler(message: types.Message, command: CommandObject):
    if not command.args or not command.args.isdigit():
        await message.answer("Используй: /remove_from_cart")
        return

    product_id = int(command.args)
    product = await get_product(product_id)
    if not product:
        await message.answer("Товар с таким ID не найден")
        return

    user_id = message.from_user.id
    await remove_from_cart(user_id, product_id)

    await message.answer(f"Товар '{product['name']}' удален из корзины")