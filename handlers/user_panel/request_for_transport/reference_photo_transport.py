from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from lexicon.lexicon_ru import lexicon


async def reference_photo_transport(callback: CallbackQuery):
    button_1 = InlineKeyboardButton(
        text='Начать осмотр',
        callback_data='start_inspection_transport'
    )
    inline_kb = [[button_1]]
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=inline_kb
    )
    await callback.message.answer(text=lexicon['reference_photo_transport'],reply_markup=keyboard)