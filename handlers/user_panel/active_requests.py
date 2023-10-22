from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from utils.db_api.schemas.house_request import HouseRequest
from utils.db_api.schemas.vehicle_request import VehicleRequest


async def active_requests(callback: CallbackQuery,state: FSMContext):
    data = await state.get_data()
    user_id = data['user_id']
    requests_for_transport = await VehicleRequest.query.where(
        VehicleRequest.user_id == user_id and VehicleRequest.status != 'finished').gino.all()

    requests_for_house = await HouseRequest.query.where(
        HouseRequest.user_id == user_id and HouseRequest.status != 'finished').gino.all()

    all_requests = requests_for_house + requests_for_transport

    statuses = dict(pending='На рассмотрении',
                    returned='Требует изменений')
    output = ''
    if all_requests:
        for request in all_requests:
            output += f'ID заявки: {request.id} Статус заявки: {statuses[request.status]}'
    else:
        output = 'Нет активных заявок'
    button = InlineKeyboardButton(
        text="В главное меню",
        callback_data='to_main'
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[button]]
    )
    await callback.message.edit_text(text=output, reply_markup=keyboard)
