from aiogram import types
from aiogram.filters import CommandObject

from config.bot_config import dp
from ADMINS import ADMIN


async def delete_admin(message: types.Message):
    user_id = message.from_user.id
    ADMIN.remove(user_id)
    kb = [
        [types.KeyboardButton(text="Подать заявку")],
        [types.KeyboardButton(text="Статус заявки")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True)
    await message.answer("Вы вернулись в режим пользователя", reply_markup=keyboard)
