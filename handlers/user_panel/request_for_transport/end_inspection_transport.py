from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from lexicon.lexicon_ru import lexicon
import utils.db_api.quick_commands as commands
from utils.db_api.schemas.vehicle_request import VehicleRequest


async def end_inspection_transport(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_id = data['user_id']
    user = await commands.select_user(user_id)

    button_1 = InlineKeyboardButton(
        text='Подать заявку',
        callback_data='apply_request'
    )
    button_2 = InlineKeyboardButton(
        text='Активные заявки',
        callback_data='active_requests'
    )
    button_3 = InlineKeyboardButton(
        text='Принятые заявки',
        callback_data='applied_requests'
    )
    inline_kb = [[button_1], [button_2], [button_3]]
    if user.is_admin:
        button4 = InlineKeyboardButton(
            text='Админ панель',
            callback_data='admin_panel'
        )
        inline_kb.append([button4])
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=inline_kb
    )
    print(data.keys())
    if 'windshield' in data and 'key' in data and 'mark_windshield' in data and 'odometer' in data \
            and 'transport_inside' in data and 'transport_outside' in data and 'vin_number' in data \
            and 'wheel' in data:
        user_id = data['user_id']
        del data['current_keyboard']
        del data['user_id']
        await commands.add_vehicle_request(user_id, **data)
        request = await VehicleRequest.query.where(VehicleRequest.user_id == user_id).gino.last()
        data = dict(user_id=user_id, current_keyboard=inline_kb)
        await callback.message.edit_text(text=lexicon['end_inspection'].format(request.id), reply_markup=keyboard)
        await state.set_data(data)
    elif len(data) < 4:
        await callback.message.edit_text(text=lexicon['early_end_inspection'], reply_markup=keyboard)
    else:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=data['current_keyboard']
        )
        await callback.message.edit_text(text=lexicon['not_end_inspection'], reply_markup=keyboard)
