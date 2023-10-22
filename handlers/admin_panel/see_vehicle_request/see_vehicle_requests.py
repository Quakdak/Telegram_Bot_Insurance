from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton, InlineKeyboardBuilder
import utils.db_api.quick_commands as commands
from .vr_callback_factory import VrCallbackFactory


async def see_vehicle_requests(callback: CallbackQuery):
    vehicle_requests = (await commands.select_all_vehicle_requests())[:100]
    callback_data_and_text = [[VrCallbackFactory(vehicle_request_id=i.id), f'Заявка {i.id}'] for i in vehicle_requests]
    if vehicle_requests:
        builder = InlineKeyboardBuilder()
        builder.adjust(3)
        for callback_data, text in callback_data_and_text:
            builder.button(text=text, callback_data=callback_data)
        builder.row(InlineKeyboardButton(text='Назад', callback_data='back_to_admin_panel'))

        await callback.message.edit_text(text='Список заявок на осмотр транспорта', reply_markup=builder.as_markup())
    else:
        button = InlineKeyboardButton(
            text='Назад',
            callback_data='back_to_admin_panel'
        )
        inline_kb = [[button]]
        keyboard = InlineKeyboardMarkup(inline_keyboard=inline_kb)
        await callback.message.edit_text(text='Список заявок на осмотр транспорта пуст', reply_markup=keyboard)


async def process_vehicle_request_press(callback: CallbackQuery,
                                        callback_data: VrCallbackFactory):
    """await callback.message.answer(text=callback_data.pack())
    await callback.answer()"""
    pass
