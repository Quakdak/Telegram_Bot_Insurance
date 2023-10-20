import os

from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv
from lexicon.lexicon_ru import lexicon
import utils.db_api.quick_commands as commands


async def start(message: Message, state: FSMContext):
    data = await state.get_data()
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    load_dotenv()

    user_id = message.from_user.id

    admin_ids = map(int, os.getenv('ADMIN_IDS').split())

    user = await commands.select_user(user_id)
    if not user:
        is_admin = False
        if user_id in admin_ids:
            is_admin = True
        await commands.add_user(user_id=user_id, first_name=message.from_user.first_name,
                                last_name=message.from_user.last_name,
                                is_admin=is_admin)

    button_1 = InlineKeyboardButton(
        text='Подать заявку',
        callback_data='apply_request'
    )
    button_2 = InlineKeyboardButton(
        text='Активные заявки',
        callback_data='avtive_requests'
    )
    button_3 = InlineKeyboardButton(
        text='Принятые заявки',
        callback_data='applied_history'
    )
    inline_kb = [[button_1], [button_2], [button_3]]
    if user_id in admin_ids:
        button4 = InlineKeyboardButton(
            text='Админ панель',
            callback_data='Admin'
        )
        inline_kb.append([button4])
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=inline_kb
    )

    await message.answer(lexicon["start"].format(user_name),
                         reply_markup=keyboard)
