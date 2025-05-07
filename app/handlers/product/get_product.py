from aiogram import Router, types
from aiogram.filters import CommandObject, Command
from app.services.product_service import get_product

router = Router()

@router.message(Command("product"))
async def product_handler(message: types.Message, command: CommandObject):
    if not command.args or not command.args.isdigit():
        await message.answer("Используй: /product <ID>")
        return

    product_id = int(command.args)
    product = await get_product(product_id)

    if not product:
        await message.answer("Товар с таким ID не найден.")
        return

    await message.answer(
        f"Подробно о товаре #{product['id']}:\n"
        f"Название: {product['name']}\n"
        f"Цена: {product['price']} руб.\n"
        f"Категория: {product['category']}"
    )
