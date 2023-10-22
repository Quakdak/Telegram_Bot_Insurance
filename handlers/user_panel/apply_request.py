from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from lexicon.lexicon_ru import lexicon


async def apply_request(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
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
    data['current_keyboard'] = inline_kb
    await state.update_data(current_keyboard=data['current_keyboard'])
    await callback.message.edit_text(text=lexicon['apply_request'], reply_markup=keyboard)