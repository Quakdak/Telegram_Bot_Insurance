from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from lexicon.lexicon_ru import lexicon


async def start_inspection_transport(callback: CallbackQuery):
    button_1 = InlineKeyboardButton(
        text='Фото VIN-номера на металле',
        callback_data='vin_number'
    )
    button_2 = InlineKeyboardButton(
        text='Фото транспортного средства снаружи',
        callback_data="transport_outside"
    )
    button_3 = InlineKeyboardButton(
        text='Фото лобового стекла',
        callback_data="windshield"
    )
    button_4 = InlineKeyboardButton(
        text='Фото маркировки лобового стекла',
        callback_data="mark_windshield"
    )
    button_5 = InlineKeyboardButton(
        text='Фото колеса в сборе',
        callback_data="wheel"
    )
    button_6 = InlineKeyboardButton(
        text='Фото показаний одометра (пробег)',
        callback_data="odometer"
    )
    button_7 = InlineKeyboardButton(
        text='Фото салона',
        callback_data="transport_inside"
    )
    button_8 = InlineKeyboardButton(
        text='Фото всех повреждений (при наличии)',
        callback_data="damage"
    )
    button_9 = InlineKeyboardButton(
        text='Фото штатных и доп. ключей',
        callback_data="key"
    )
    inline_kb = [[button_1], [button_2],[button_3],[button_4],[button_5],[button_6],[button_7],[button_8],[button_9]]
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=inline_kb
    )
    await callback.message.edit_text(text=lexicon['start_inspection'],reply_markup=keyboard)