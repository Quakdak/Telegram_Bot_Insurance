from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

import utils.db_api.quick_commands as commands


async def accept_house_request(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    house_request_id = data['house_request_id']
    house_request = await commands.select_vehicle_request(house_request_id)
    await state.clear()
    await house_request.update(status='accepted').apply()
    await callback.answer(text='Заявка успешно принята')
    button = InlineKeyboardButton(
        text='Назад',
        callback_data='back_to_admin_panel'
    )
    inline_kb = [[button]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_kb)
    await callback.message.edit_text(text='Назад', reply_markup=keyboard)


async def return_house_request(callback: CallbackQuery,
                               state: FSMContext):
    data = await state.get_data()
    house_request_id = data['house_request_id']
    house_request = await commands.select_vehicle_request(house_request_id)
    await state.clear()
    await callback.message.edit_text(text='Ведите сообшение пользователю: ')

    await house_request.update(status='returned').apply()
    await callback.answer(text='Заявка успешно отправлена обратно')
    button = InlineKeyboardButton(
        text='Назад',
        callback_data='back_to_admin_panel'
    )
    inline_kb = [[button]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_kb)
    await callback.message.edit_text(text='Назад', reply_markup=keyboard)


async def decline_house_request(callback: CallbackQuery,
                                state: FSMContext):
    data = await state.get_data()
    house_request_id = data['house_request_id']
    house_request = await commands.select_vehicle_request(house_request_id)
    await state.clear()
    await house_request.update(status='declined').apply()
    await callback.answer(text='Заявка успешно отклонена')
    button = InlineKeyboardButton(
        text='Назад',
        callback_data='back_to_admin_panel'
    )
    inline_kb = [[button]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_kb)
    await callback.message.edit_text(text='Вернуться в панель администратора', reply_markup=keyboard)
