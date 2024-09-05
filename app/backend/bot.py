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

def generate_jwt(data, secret_key):
    payload = data.copy()
    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)  # Время жизни токена
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return token

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
    secret_key = "your_secret_key"
    token = generate_jwt(user_data, secret_key)
    web_app_url = f"{settings.HTTPS_URL}/?token={token}"
    web_app = WebAppInfo(url=web_app_url)
    markup = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="Open Mini App", web_app=web_app)]]
    )
    await bot.send_message(
        message.chat.id, "Click to open the mini app", reply_markup=markup
    )
