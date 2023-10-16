from aiogram import types
from config.bot_config import dp

@dp.message(commands=["start"])
async def start(message: types.Message):
    user_name = message.from_user.first_name
    kb = [
        [types.KeyboardButton(text="Подать заявку")],
        [types.KeyboardButton(text="Статус заявки")],
        [types.KeyboardButton(text="История заявок")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True)
    await message.answer(f"Привет, {user_name}! Я твой помощник по страхованию Страх-cтрахыч",reply_markup=keyboard)