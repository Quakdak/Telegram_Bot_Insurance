from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from lexicon.lexicon_ru import lexicon


async def reference_photo_transport(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    button_1 = InlineKeyboardButton(
        text='Начать осмотр',
        callback_data='start_inspection_transport'
    )
    inline_kb = [[button_1]]
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=inline_kb
    )
    data['current_keyboard'] = inline_kb
    await state.update_data(current_keyboard=data['current_keyboard'])
    await callback.message.edit_text(text=lexicon['reference_photo_transport'],reply_markup=keyboard)