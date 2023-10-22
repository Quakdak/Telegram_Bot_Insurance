from aiogram.types import Message, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
from lexicon.lexicon_ru import lexicon


async def error(message: Message,state: FSMContext):
    data = await state.get_data()
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=data['current_keyboard']
    )
    await message.answer(text=lexicon['error'], reply_markup=keyboard)
