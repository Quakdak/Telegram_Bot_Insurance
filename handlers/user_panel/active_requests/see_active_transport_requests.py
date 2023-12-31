from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton, InlineKeyboardBuilder

from lexicon.lexicon_ru import lexicon
from utils.db_api.schemas.vehicle_request import VehicleRequest
from handlers.user_panel.active_requests.callback_data_class import VrActiveCallbackFactory
import utils.db_api.quick_commands as commands


async def see_active_transport_requests(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_id = data['user_id']

    requests_for_vehicle = await VehicleRequest.query.where(
        VehicleRequest.user_id == user_id).where(VehicleRequest.status != 'accepted').gino.all()

    if requests_for_vehicle:
        callback_data_and_text = [
            [VrActiveCallbackFactory(request_id=request.id), f'Заявка {request.id}'] for request in
            requests_for_vehicle]
        builder = InlineKeyboardBuilder()
        for callback_data, number in callback_data_and_text:
            builder.button(text=f'{number}', callback_data=callback_data)
        builder.row(InlineKeyboardButton(text='В главное меню', callback_data='to_main'))
        data['current_keyboard'] = builder
        await state.update_data(current_keyboard=data['current_keyboard'])
        await callback.message.edit_text(text='Список активных заявок на транспорт', reply_markup=builder.as_markup())
    else:
        button = InlineKeyboardButton(
            text="В главное меню",
            callback_data='to_main'
        )
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[[button]]
        )
        data['current_keyboard'] = [[button]]
        await state.update_data(current_keyboard=data['current_keyboard'])
        await callback.message.edit_text(text='Нет активных заявок', reply_markup=keyboard)


async def process_transport_request_press(callback: CallbackQuery, callback_data: VrActiveCallbackFactory,
                                          state: FSMContext):
    data = callback_data.pack().split(':')
    transport_request_id = data[-1]

    request = await commands.select_vehicle_request(int(transport_request_id))

    if request.status == 'pending':
        button = InlineKeyboardButton(
            text="В главное меню",
            callback_data='to_main'
        )
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[[button]]
        )
        await state.update_data(current_keyboard=[[button]])
        await callback.message.edit_text(text='Ваша заявка на рассмотрении', reply_markup=keyboard)
    else:
        button = InlineKeyboardButton(
            text="В главное меню",
            callback_data='to_main'
        )
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[[button]]
        )
        await state.update_data(current_keyboard=[[button]])
        await callback.message.edit_text(
            text='Ваше заявление {} было отправлено на доработку, заполните новое заявление, следуя комментарию страховщика'.format(
                request.id), reply_markup=keyboard)
        await request.delete()
