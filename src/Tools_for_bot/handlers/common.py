from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from src.Tools_for_bot.services.users_service import users_service

router = Router(name="common_commands")


@router.message(CommandStart)
async def cmd_start(message: Message):
    user = users_service.get_or_create_user(message.from_user.id)
    
    if user.is_registered():
        await message.answer(
            f"Привет, {user.name}! Рад видеть тебя снова!\n"
            f"Ты уже зарегистрирован в системе."
        )
    else:
        await message.answer(
            "Привет! Добро пожаловать в нашего бота!\n"
            "Для регистрации используй команду /register"
        )


@router.message(Command("help"))
async def cmd_help(message: Message):
    help_text = (
        "<b>Доступные команды:</b>\n\n"
        "/start - Начать работу с ботом\n"
        "/register - Регистрация в системе\n"
        "/profile - Просмотр своего профиля\n"
        "/cancel - Отмена текущего действия\n"
        "/help - Показать это сообщение"
    )
    
    await message.answer(help_text, parse_mode="HTML")


@router.message(Command("profile"))
async def cmd_profile(message: Message):
    user = users_service.get_user(message.from_user.id)
    
    if user is None or not user.is_registered():
        await message.answer(
            "Вы еще не зарегистрированы!\n"
            "Используйте команду /register для регистрации."
        )
        return
    
    profile_text = (
        "<b>Ваш профиль:</b>\n\n"
        f"Имя: {user.name}\n"
        f"Возраст: {user.age}\n"
        f"Email: {user.email}\n"
        f"Дата регистрации: {user.created_at.strftime('%d.%m.%Y %H:%M')}"
    )
    
    await message.answer(profile_text, parse_mode="HTML")