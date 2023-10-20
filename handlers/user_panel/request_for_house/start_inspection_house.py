from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from lexicon.lexicon_ru import lexicon


async def start_inspection_house(callback: CallbackQuery, state: FSMContext):
    button_1 = InlineKeyboardButton(
        text='Фото общего вида участка',
        callback_data='general_view_house'
    )
    button_2 = InlineKeyboardButton(
        text='Фото наружных инженерных коммуникаций',
        callback_data="outside_engineering"
    )
    button_3 = InlineKeyboardButton(
        text='Фото фасадов строений',
        callback_data="facades_buildings"
    )
    button_4 = InlineKeyboardButton(
        text='Фото механической защиты окон и дверей',
        callback_data="mechanical_protection"
    )
    button_5 = InlineKeyboardButton(
        text='Фото входных дверей',
        callback_data="front_door"
    )
    button_6 = InlineKeyboardButton(
        text='Фото внутреннего инженерного оборудования',
        callback_data="inside_engineering"
    )
    button_7 = InlineKeyboardButton(
        text='Фото пожарной сигнализации',
        callback_data="fire_alarm_system"
    )
    button_8 = InlineKeyboardButton(
        text='Фото охранной сигнализации',
        callback_data="security_alarm_system"
    )
    button_9 = InlineKeyboardButton(
        text='Фото внутренней отделки',
        callback_data="interior"
    )
    button_10 = InlineKeyboardButton(
        text='Фото оконных блоков',
        callback_data="window"
    )
    button_11 = InlineKeyboardButton(
        text='Фото дефектов',
        callback_data="defect"
    )
    button_12 = InlineKeyboardButton(
        text='Фото домашнего имущества',
        callback_data="household_property"
    )
    button_13 = InlineKeyboardButton(
        text='Фото забора',
        callback_data="fence"
    )
    button_14 = InlineKeyboardButton(
        text='Закончить осмотр',
        callback_data='end_inspection_house'
    )
    inline_kb = [[button_1], [button_2], [button_3], [button_4], [button_5], [button_6], [button_7],
                 [button_8], [button_9], [button_10], [button_11], [button_12], [button_13], [button_14]]
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=inline_kb
    )
    await state.update_data(current_keyboard=inline_kb)
    await callback.message.edit_text(text=lexicon['start_inspection'], reply_markup=keyboard)
