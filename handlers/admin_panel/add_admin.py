from aiogram import types
from aiogram.filters import CommandObject

from ADMINS import ADMIN


async def add_admin(message: types.Message):
    user_id = message.from_user.id
    ADMIN.add(user_id)
    kb = [
        [types.KeyboardButton(text="Активные заявки")],
        [types.KeyboardButton(text="Вернуться в режим пользователя")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True)
    await message.answer("Вы стали страховщиком.", reply_markup=keyboard)
