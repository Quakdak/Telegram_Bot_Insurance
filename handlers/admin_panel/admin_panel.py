from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from lexicon.lexicon_ru import lexicon


async def admin(callback: CallbackQuery):
    button_1 = InlineKeyboardButton(
        text='Просмотреть текущие заявки на транспорт',
        callback_data='transport_requests'
    )
    button_4 = InlineKeyboardButton(
        text='Просмотреть текущие заявки на недвижимость',
        callback_data='house_requests'
    )
    button_3 = InlineKeyboardButton(
        text='Вернуться в режим пользователя',
        callback_data='main_menu'
    )
    button_2 = InlineKeyboardButton(
        text='История заявок',
        callback_data='applied_history'
    )
    inline_kb = [[button_1], [button_4], [button_2], [button_3]]
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=inline_kb
    )
    await callback.message.edit_text(text=lexicon['admin'], reply_markup=keyboard)
