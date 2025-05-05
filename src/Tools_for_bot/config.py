import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    DB_PATH: str = os.getenv("DB_PATH", "users.db")

config = Config()

if not config.BOT_TOKEN:
    raise ValueError("Не найден токен бота. Убедитесь, что переменная BOT_TOKEN задана в .env файле")