from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from .states import RegistrationStates
from ..services.users_service import users_service
from . import common, registration

router = Router(name="registration")


@router.message(Command("register"))
async def cmd_register(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = users_service.get_user(user_id)
    
    if user and user.is_registered():
        await message.answer(
            f"Вы уже зарегистрированы в системе!\n\n"
            f"Ваши данные:\n"
            f"Имя: {user.name}\n"
            f"Возраст: {user.age}\n"
            f"Email: {user.email}"
        )
        return
    
    if not user:
        user = users_service.create_user(user_id)

    await state.set_state(RegistrationStates.waiting_for_name)
    await message.answer(
        "Начинаем процесс регистрации!\n\n"
        "Пожалуйста, введите ваше имя"
    )


@router.message(StateFilter(RegistrationStates.waiting_for_name))
async def process_name(message: Message, state: FSMContext):
    name = message.text.strip()
    
    user = users_service.get_user(message.from_user.id)
    
    user.name = name
    users_service.update_user(user)
    
    await state.update_data(name=name)
    
    await state.set_state(RegistrationStates.waiting_for_age)
    await message.answer(
        f"Приятно познакомиться, {name}! \n\n"
        "Теперь введите ваш возраст (только число)"
    )


@router.message(StateFilter(RegistrationStates.waiting_for_age))
async def process_age(message: Message, state: FSMContext):
    age = int(message.text.strip())
    
    user = users_service.get_user(message.from_user.id)
    
    user.age = age
    users_service.update_user(user)

    await state.update_data(age=age)
    
    await state.set_state(RegistrationStates.waiting_for_email)
    await message.answer(
        f"Отлично! \n\n"
        "Теперь введите ваш email"
    )


@router.message(StateFilter(RegistrationStates.waiting_for_email))
async def process_email(message: Message, state: FSMContext):
    email = message.text.strip()
    
    user = users_service.get_user(message.from_user.id)
    user_data = await state.get_data()
    
    user.email = email
    users_service.update_user(user)
    
    await state.clear()
    
    registration_message = (
        "<b>Регистрация успешно завершена!</b>\n\n"
        "<b>Ваши данные:</b>\n"
        f"Имя: {user.name}\n"
        f"Возраст: {user.age}\n"
        f"Email: {user.email}\n\n"
        "Теперь вы можете использовать все функции бота.\n"
        "Введите /help для просмотра доступных команд."
    )
    
    await message.answer(registration_message, parse_mode="HTML")


@router.message(Command("cancel"), StateFilter(RegistrationStates))
async def cancel_registration(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.clear()
        await message.answer(
            "Регистрация отменена.\n\n"
            "Вы можете начать снова, используя команду /register"
        )
    else:
        await message.answer("В данный момент нет активного процесса регистрации.")