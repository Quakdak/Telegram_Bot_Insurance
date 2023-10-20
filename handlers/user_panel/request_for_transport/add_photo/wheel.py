from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from handlers.user_panel.state_request.state_request_transport import request_transport
from lexicon.lexicon_ru import lexicon


async def wheel(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=lexicon['wheel'])
    await state.set_state(request_transport.wait_wheel)


async def getting_wheel(message: Message, state: FSMContext):
    data = await state.get_data()
    if 'wheel' in data:
        data['wheel'].append(message.photo[-1].file_id)
    else:
        data['wheel'] = [message.photo[-1].file_id]
    button_1 = InlineKeyboardButton(
        text='Добавить еще',
        callback_data="add_more_wheel"
    )
    button_2 = InlineKeyboardButton(
        text='Закончить',
        callback_data='end_add_wheel'
    )
    kb = [[button_1], [button_2]]
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=kb
    )
    await message.answer(text=lexicon['add_more'], reply_markup=keyboard)


async def got_wheel(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    button = InlineKeyboardButton(
        text='✅Фото колеса в сборе',
        callback_data="done"
    )
    for num in range(len(data['current_keyboard'])):
        if data['current_keyboard'][num][0].callback_data == 'wheel':
            data['current_keyboard'][num][0] = button
            break
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=data['current_keyboard']
    )
    await state.update_data(current_keyboard=data['current_keyboard'])
    await callback.message.edit_text(text=lexicon['got_photo'], reply_markup=keyboard)
    await state.set_state(state=None)
