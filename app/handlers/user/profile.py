from aiogram import Router, types, F
from app.services.user_service import get_user_profile


router = Router()

@router.message(F.text == "/profile")
async def handle_profile(message: types.Message):
    telegram_id = message.from_user.id
    user = await get_user_profile(telegram_id)

    if user:
        role = "Admin" if user.get("is_admin") else "User"
        text = (
            f"Ваш профиль:\n"
            f"Имя: {user.get('name')}\n"
            f"Telegram ID: {telegram_id}\n"
            f"Роль: {role}"
        )
    else:
        text = "Профиль не найден. Попробуйте /start для регистрации."

    await message.answer(text)