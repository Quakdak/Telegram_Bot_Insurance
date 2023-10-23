from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from utils.db_api.schemas.house_request import HouseRequest
from utils.db_api.schemas.vehicle_request import VehicleRequest


async def applied_requests(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_id = data['user_id']

    requests_for_transport = await VehicleRequest.query.where(
        VehicleRequest.user_id == user_id).where(VehicleRequest.status == 'accepted').gino.all()

    requests_for_house = await HouseRequest.query.where(
        HouseRequest.user_id == user_id).where(HouseRequest.status == 'accepted').gino.all()

    all_requests = requests_for_house + requests_for_transport

    output = ''
    if all_requests:
        for request in all_requests:
            output += f'ID заявки: {request.id} Статус заявки: Принята'
    else:
        output = 'Нет принятых заявок'
    button = InlineKeyboardButton(
        text="В главное меню",
        callback_data='to_main'
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[button]]
    )
    data['current_keyboard'] = [[button]]
    await state.update_data(current_keyboard=data['current_keyboard'])
    await callback.message.edit_text(text=output, reply_markup=keyboard)
