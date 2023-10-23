from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

from config.bot_config import bot
from ..states.vehicle_request_review import FSMVehicleRequestReview
import utils.db_api.quick_commands as commands


async def accept_vehicle_request(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    vehicle_request_id = data['vehicle_request_id']
    vehicle_request = await commands.select_vehicle_request(vehicle_request_id)
    user_id = vehicle_request.user_id
    await state.clear()
    await state.update_data(user_id=user_id)
    await vehicle_request.update(status='accepted').apply()
    await callback.answer(text='Заявка успешно принята')
    button = InlineKeyboardButton(
        text='Назад',
        callback_data='back_to_admin_panel'
    )
    inline_kb = [[button]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_kb)
    await callback.message.edit_text(text='Назад', reply_markup=keyboard)


async def begin_return_vehicle_request(callback: CallbackQuery,
                                       state: FSMContext):
    await callback.message.edit_text(text='Введите сообшение пользователю: ')
    await state.set_state(FSMVehicleRequestReview.write_message_to_user)


async def write_comment_to_vehicle_request(message: Message, state: FSMContext):
    data = await state.get_data()

    vehicle_request_id = data['vehicle_request_id']
    vehicle_request = await commands.select_vehicle_request(vehicle_request_id)
    user_id = vehicle_request.user_id
    await state.clear()
    await state.update_data(user_id=user_id)
    msg = message.text
    text = f'Ваша заявка на осмотр транспорта №{vehicle_request_id} не прошла проверку администратора\n' \
           f'Попробуйте еще раз\n' \
           f'Сообщение администратора: \n' \
           f'{msg}'
    await bot.send_message(chat_id=user_id, text=text)

    await vehicle_request.update(status='returned').apply()
    button = InlineKeyboardButton(
        text='Назад',
        callback_data='back_to_admin_panel'
    )
    inline_kb = [[button]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_kb)
    await message.answer(text='Заявка успешно отправлена на доработку', reply_markup=keyboard)