from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from lexicon.lexicon_ru import lexicon


async def request_for_transport(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    button_1 = InlineKeyboardButton(
        text='Справка',
        callback_data='reference_photo_transport'
    )
    inline_kb = [[button_1]]
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=inline_kb
    )
    data['current_keyboard'] = inline_kb
    await state.update_data(current_keyboard=data['current_keyboard'])
    await callback.message.edit_text(text=lexicon['request_for'], reply_markup=keyboard)
