from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from lexicon.lexicon_ru import lexicon


async def active_request(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    button_1 = InlineKeyboardButton(
        text='На транспорт',
        callback_data='see_active_transport_requests'
    )
    button_2 = InlineKeyboardButton(
        text='На загородный дом',
        callback_data='see_active_house_requests'
    )
    inline_kb = [[button_1], [button_2]]
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=inline_kb
    )
    data['current_keyboard'] = inline_kb
    await state.update_data(current_keyboard=data['current_keyboard'])
    await callback.message.edit_text(text=lexicon['active_requests'], reply_markup=keyboard)