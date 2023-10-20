from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from handlers.user_panel.state_request.state_request_house import request_house
from lexicon.lexicon_ru import lexicon


async def front_door(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=lexicon['front_door'])
    await state.set_state(request_house.wait_front_door)


async def getting_front_door(message: Message, state: FSMContext):
    data = await state.get_data()
    if 'front_door' in data:
        data['front_door'].append(message.photo[-1].file_id)
    else:
        data['front_door'] = [message.photo[-1].file_id]
    button_1 = InlineKeyboardButton(
        text='Добавить еще',
        callback_data="add_more_front_door"
    )
    button_2 = InlineKeyboardButton(
        text='Закончить',
        callback_data='end_add_front_door'
    )
    kb = [[button_1], [button_2]]
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=kb
    )
    await message.answer(text=lexicon['add_more'], reply_markup=keyboard)


async def got_front_door(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    button = InlineKeyboardButton(
        text='✅Фото входных дверей',
        callback_data="done"
    )
    for num in range(len(data['current_keyboard'])):
        if data['current_keyboard'][num][0].callback_data == 'front_door':
            data['current_keyboard'][num][0] = button
            break
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=data['current_keyboard']
    )
    await state.update_data(current_keyboard=data['current_keyboard'])
    await callback.message.edit_text(text=lexicon['got_photo'], reply_markup=keyboard)
    await state.set_state(state=None)
