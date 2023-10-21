from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from lexicon.lexicon_ru import lexicon


async def admin(callback: CallbackQuery):
    button_1 = InlineKeyboardButton(
        text='Просмотреть текущие заявки',
        callback_data='active_requests'
    )
    button_3 = InlineKeyboardButton(
        text='Вернуться в режим пользователя',
        callback_data='main_menu'
    )
    button_2 = InlineKeyboardButton(
        text='История заявок',
        callback_data='applied_history'
    )
    inline_kb = [[button_1], [button_2], [button_3]]
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=inline_kb
    )
    await callback.message.edit_text(text='Админ-панель', reply_markup=keyboard)
