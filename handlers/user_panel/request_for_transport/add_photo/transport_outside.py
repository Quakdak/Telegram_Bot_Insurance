from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from handlers.user_panel.state_request.state_request_transport import request_transport
from lexicon.lexicon_ru import lexicon


async def transport_outside(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=lexicon['transport_outside'])
    await state.set_state(request_transport.wait_transport_outside)


async def getting_transport_outside(message: Message, state: FSMContext):
    data = await state.get_data()
    if 'transport_outside' in data:
        data['transport_outside'].append(message.photo[-1].file_id)
    else:
        data['transport_outside'] = [message.photo[-1].file_id]
    button_1 = InlineKeyboardButton(
        text='Добавить еще',
        callback_data="add_more_transport_outside"
    )
    button_2 = InlineKeyboardButton(
        text='Закончить',
        callback_data='end_add_transport_outside'
    )
    kb = [[button_1], [button_2]]
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=kb
    )
    await message.answer(text=lexicon['add_more'], reply_markup=keyboard)


async def got_transport_outside(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    button = InlineKeyboardButton(
        text='✅Фото транспортного средства снаружи',
        callback_data="done"
    )
    for num in range(len(data['current_keyboard'])):
        if data['current_keyboard'][num][0].callback_data == 'transport_outside':
            data['current_keyboard'][num][0] = button
            break
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=data['current_keyboard']
    )
    await state.update_data(current_keyboard=data['current_keyboard'])
    await callback.message.edit_text(text=lexicon['got_photo'], reply_markup=keyboard)
    await state.set_state(state=None)
