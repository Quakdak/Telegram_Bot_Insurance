from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton, InlineKeyboardBuilder
from utils.db_api.schemas.house_request import HouseRequest
from handlers.user_panel.active_requests.callback_data_class import HrActiveCallbackFactory
import utils.db_api.quick_commands as commands


async def see_active_house_requests(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_id = data['user_id']

    requests_for_house = await HouseRequest.query.where(
        HouseRequest.user_id == user_id).where(HouseRequest.status != 'accepted').gino.all()

    if requests_for_house:
        callback_data_and_text = [
            [HrActiveCallbackFactory(HR_request_id=request.id), f'Заявка {request.id}'] for request in
            requests_for_house]
        builder = InlineKeyboardBuilder()
        for callback_data, number in callback_data_and_text:
            builder.button(text=f'{number}', callback_data=callback_data)
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
        await state.update_data(current_keyboard=[[button]])
        await callback.message.edit_text(text='Нет активных заявок', reply_markup=keyboard)


async def process_active_house_request_press(callback: CallbackQuery, callback_data: HrActiveCallbackFactory,
                                             state: FSMContext):
    data = callback_data.pack().split(':')
    house_request_id = data[-1]
    print(callback_data)
    request = await commands.select_house_request(int(house_request_id))

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
