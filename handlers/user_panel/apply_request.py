from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from lexicon.lexicon_ru import lexicon


async def apply_request(callback: CallbackQuery):
    button_1 = InlineKeyboardButton(
        text='На транспорт',
        callback_data='request_for_transport'
    )
    button_2 = InlineKeyboardButton(
        text='На загородный дом',
        callback_data='request_for_house'
    )
    inline_kb = [[button_1], [button_2]]
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=inline_kb
    )
    await callback.message.answer(text=lexicon['apply_request'], reply_markup=keyboard)