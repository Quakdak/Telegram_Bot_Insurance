from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from lexicon.lexicon_ru import lexicon


async def reference_photo_house(callback: CallbackQuery):
    button_1 = InlineKeyboardButton(
        text='Начать осмотр',
        callback_data='start_inspection_house'
    )
    inline_kb = [[button_1]]
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=inline_kb
    )
    await callback.message.edit_text(text=lexicon['reference_photo_house'],reply_markup=keyboard)