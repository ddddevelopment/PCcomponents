import asyncio
from app.database import user_repository


async def register_user(telegram_id: int, name: str) -> bool:
    user = await asyncio.to_thread(user_repository.get_user_by_telegram_id, telegram_id)
    if user:
        return False

    await asyncio.to_thread(user_repository.create_user, telegram_id, name)
    return True
