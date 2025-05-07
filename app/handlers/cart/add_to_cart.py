from aiogram import Router, types
from aiogram.filters import Command, CommandObject

from app.services.product_service import get_product
from app.services.cart_service import add_to_cart

router = Router()

@router.message(Command("add_to_cart"))
async def add_to_cart_handler(message: types.Message, command: CommandObject):
    if not command.args or not command.args.isdigit():
        await message.answer("Используй: /add_to_cart <ID>")
        return

    product_id = int(command.args)
    product = await get_product(product_id)
    if not product:
        await message.answer("Товар с таким ID не найден")
        return

    user_id = message.from_user.id
    await add_to_cart(user_id, product_id)

    await message.answer(f"Товар '{product['name']}' добавлен в корзину")