from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from lexicon.lexicon_ru import lexicon


async def request_for_house(callback: CallbackQuery):
    button_1 = InlineKeyboardButton(
        text='Справка',
        callback_data='reference_photo_house'
    )
    inline_kb = [[button_1]]
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=inline_kb
    )
    await callback.message.edit_text(text=lexicon['request_for'],reply_markup=keyboard)