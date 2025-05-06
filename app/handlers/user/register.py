from aiogram import Router, types, F
from app.services.user_service import register_user

router = Router()

@router.message(F.text == "/start")
async def handle_start(message: types.Message):
    telegram_id = message.from_user.id
    name = message.from_user.full_name

    is_new = await register_user(telegram_id, name)

    if is_new:
        await message.answer("✅ Вы успешно зарегистрированы!")
    else:
        await message.answer("👋 Вы уже зарегистрированы.")
