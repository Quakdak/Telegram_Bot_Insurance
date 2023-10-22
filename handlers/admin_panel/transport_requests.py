from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from lexicon.lexicon_ru import lexicon


async def transport_requests(callback: CallbackQuery):
    # Вывод активных заявок на транспорт(я без понятия как это будет выглядеть)
    button_1 = InlineKeyboardButton(
        text='Вернуться в главное меню',
        callback_data='main_menu'
    )

    inline_kb = [[button_1]]
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=inline_kb
    )
    await callback.message.edit_text(text=lexicon['house_requests'], reply_markup=keyboard)