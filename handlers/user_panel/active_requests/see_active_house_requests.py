from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton, InlineKeyboardBuilder
from utils.db_api.schemas.house_request import HouseRequest
from handlers.admin_panel.see_house_request.hr_callback_factory import HrCallbackFactory


async def see_active_house_requests(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_id = data['user_id']
    
    requests_for_house = await HouseRequest.query.where(
        HouseRequest.user_id == user_id).where(HouseRequest.status != 'accepted').gino.all()

    statuses = dict(pending='На рассмотрении',
                    returned='Требует изменений')

    if requests_for_house:
        callback_data_and_text = [
            [HrCallbackFactory(house_request_id=request.id), f'Заявка {request.id}',
             f'Статус {statuses[request.status.rstrip()]}'] for request in requests_for_house]
        builder = InlineKeyboardBuilder()
        for callback_data, number, status in callback_data_and_text:
            builder.button(text=f'{number} {status}', callback_data=callback_data)
        builder.row(InlineKeyboardButton(text='В главное меню', callback_data='to_main'))
        data['current_keyboard'] = builder
        await state.update_data(current_keyboard=data['current_keyboard'])
        await callback.message.edit_text(text='Список активных заявок на дом', reply_markup=builder.as_markup())
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


"""async def process_house_request_press(callback: CallbackQuery, callback_data: HrCallbackFactory):
    data = callback_data.pack().split(':')
    house_request_id = data[0]

    requests_for_house = await HouseRequest.query.where(
        HouseRequest.id == house_request_id).where(HouseRequest.status != 'accepted').gino.all()

    output = f'Сообщение от страховщика:\n{}'"""