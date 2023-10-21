import os

from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv
from lexicon.lexicon_ru import lexicon


async def main_menu(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_id = callback.message.from_user.id
    user_name = callback.message.from_user.first_name
    load_dotenv()
    admin_ids = map(int, os.getenv('ADMIN_IDS').split())

    button_1 = InlineKeyboardButton(
        text='Подать заявку',
        callback_data='apply_request'
    )
    button_2 = InlineKeyboardButton(
        text='Активные заявки',
        callback_data='active_requests'
    )
    button_3 = InlineKeyboardButton(
        text='Принятые заявки',
        callback_data='applied_history'
    )
    inline_kb = [[button_1], [button_2], [button_3]]
    button4 = InlineKeyboardButton(
        text='Админ панель',
        callback_data='admin'
     )
    inline_kb.append([button4])
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=inline_kb
    )

    await callback.message.edit_text(text=lexicon["start"].format(user_name), reply_markup=keyboard)
