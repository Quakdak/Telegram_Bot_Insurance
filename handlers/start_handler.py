import os

from aiogram import types
from dotenv import load_dotenv

import utils.db_api.quick_commands as commands

load_dotenv()


async def start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Подать заявку")],
        [types.KeyboardButton(text="Статус заявки")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True)

    user_id = message.from_user.id

    user = await commands.select_user(user_id)
    if user:
        await message.answer(f"Привет, {user.first_name}! Я твой помощник по страхованию Страх-cтрахыч",
                             reply_markup=keyboard)
    else:
        is_admin = False
        admin_ids = map(int, os.getenv('ADMIN_IDS').split())
        if user_id in admin_ids:
            is_admin = True
        await commands.add_user(user_id=user_id, first_name=message.from_user.first_name,
                                last_name=message.from_user.last_name,
                                is_admin=is_admin)
        await message.answer(f"Привет, {user.first_name}! Я твой помощник по страхованию Страх-cтрахыч",
                             reply_markup=keyboard)
