from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardMarkup
from lexicon.lexicon_ru import lexicon


async def done(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=data['current_keyboard']
    )
    await callback.message.edit_text(text=lexicon['done'], reply_markup=keyboard)
