from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from handlers.user_panel.state_request.state_request_transport import request_transport
from lexicon.lexicon_ru import lexicon


async def odometer(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=lexicon['odometer'])
    await state.set_state(request_transport.wait_odometer)


async def getting_odometer(message: Message, state: FSMContext):
    data = await state.get_data()
    if 'odometer' in data:
        data['odometer'].append(message.photo[-1].file_id)
    else:
        data['odometer'] = [message.photo[-1].file_id]
    button_1 = InlineKeyboardButton(
        text='Добавить еще',
        callback_data="add_more_odometer"
    )
    button_2 = InlineKeyboardButton(
        text='Закончить',
        callback_data='end_add_odometer'
    )
    kb = [[button_1], [button_2]]
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=kb
    )
    await message.answer(text=lexicon['add_more'], reply_markup=keyboard)


async def got_odometer(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    button = InlineKeyboardButton(
        text='✅Фото показаний одометра (пробег)',
        callback_data="done"
    )
    for num in range(len(data['current_keyboard'])):
        if data['current_keyboard'][num][0].callback_data == 'odometer':
            data['current_keyboard'][num][0] = button
            break
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=data['current_keyboard']
    )
    await callback.message.edit_text(text=lexicon['got_photo'], reply_markup=keyboard)
    await state.set_state(state=None)
