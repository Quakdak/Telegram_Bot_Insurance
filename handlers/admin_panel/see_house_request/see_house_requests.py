from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton, InlineKeyboardBuilder

from handlers.admin_panel.see_house_request.hr_callback_factory import HrCallbackFactory
import utils.db_api.quick_commands as commands


async def see_house_requests(callback: CallbackQuery):
    house_requests = (await commands.select_all_house_requests())[:100]
    callback_data_and_text = [[HrCallbackFactory(house_request_id=i.id), f'Заявка {i.id}'] for i in house_requests]
    if house_requests:
        builder = InlineKeyboardBuilder()
        builder.adjust(3)
        for callback_data, text in callback_data_and_text:
            builder.button(text=text, callback_data=callback_data)
        builder.row(InlineKeyboardButton(text='Назад', callback_data='back_to_admin_panel'))

        await callback.message.edit_text(text='Список заявок на осмотр дома', reply_markup=builder.as_markup())

    else:
        button = InlineKeyboardButton(
            text='Назад',
            callback_data='back_to_admin_panel'
        )
        inline_kb = [[button]]
        keyboard = InlineKeyboardMarkup(inline_keyboard=inline_kb)
        await callback.message.edit_text(text='Список заявок на осмотр дома пуст', reply_markup=keyboard)


async def process_house_request_press(callback: CallbackQuery,
                                      callback_data: HrCallbackFactory):
    data = callback_data.pack().split(':')
    house_request_id = data[-1]
    house_request = await commands.select_house_request(house_request_id)



