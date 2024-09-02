from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from backend.database.settings import settings
from aiogram.filters import Command
import logging
import jwt
import datetime


logging.basicConfig(level=logging.INFO)


bot = Bot(token=settings.TG_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    user_data = {
        "tg_user_id": int(message.from_user.id),
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
        "username": message.from_user.username,
        "date_of_birth": None, 
        "created_at": None, 
        "updated_at": None,
    }

    query_params = "&".join(
        f"{key}={value if value is not None else 'none'}"
        for key, value in user_data.items()
    )
    web_app_url = f"https://16cd-94-181-225-220.ngrok-free.app/?{query_params}"

    web_app = WebAppInfo(url=web_app_url)
    markup = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="Open Mini App", web_app=web_app)]]
    )
    await bot.send_message(
        message.chat.id, "Click to open the mini app", reply_markup=markup
    )
