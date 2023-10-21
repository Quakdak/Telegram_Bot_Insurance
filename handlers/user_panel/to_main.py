from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
import utils.db_api.quick_commands as commands


async def to_main(callback: CallbackQuery):
    user_id = callback.message.from_user.id
    user = await commands.select_user(user_id)
    print(user)

    button_1 = InlineKeyboardButton(
        text='Подать заявку',
        callback_data='apply_request'
    )
    button_2 = InlineKeyboardButton(
        text='Активные заявки',
        callback_data='avtive_requests'
    )
    button_3 = InlineKeyboardButton(
        text='Принятые заявки',
        callback_data='applied_history'
    )
    inline_kb = [[button_1], [button_2], [button_3]]
    if user.is_admin:
        button4 = InlineKeyboardButton(
            text='Админ панель',
            callback_data='Admin'
        )
        inline_kb.append([button4])
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=inline_kb
    )
    await callback.message.edit_text(text='Вы вернулись в главное меню', reply_markup=keyboard)
