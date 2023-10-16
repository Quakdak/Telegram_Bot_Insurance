from aiogram import types
from aiogram.filters import CommandObject

from config.bot_config import dp


async def start(message: types.Message):
    user_name = message.from_user.first_name
    kb = [
        [types.KeyboardButton(text="Подать заявку")],
        [types.KeyboardButton(text="Статус заявки")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True)
    await message.answer(f"Привет, {user_name}! Я твой помощник по страхованию Страх-cтрахыч", reply_markup=keyboard)
