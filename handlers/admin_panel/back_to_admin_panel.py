from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton


async def back_to_admin_panel(callback: CallbackQuery):
    button_1 = InlineKeyboardButton(
        text='Заявки на осмотр транспорта',
        callback_data='see_vehicle_requests'
    )
    button_2 = InlineKeyboardButton(
        text='Заявки на осмотр дома',
        callback_data='see_house_requests'
    )
    button_3 = InlineKeyboardButton(
        text='В главное меню',
        callback_data='to_main'
    )
    inline_kb = [[button_1], [button_2], [button_3]]

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=inline_kb
    )
    await callback.message.edit_text(text='Вы вернулись в панель администратора',
                                     reply_markup=keyboard)
