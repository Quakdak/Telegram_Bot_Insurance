from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from handlers.user_panel.state_request.state_request_house import request_house
from lexicon.lexicon_ru import lexicon
from utils.get_photo import get_photo


async def fire_alarm_system(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=lexicon['fire_alarm_system'])
    await state.set_state(request_house.wait_fire_alarm_system)


async def getting_fire_alarm_system(message: Message, state: FSMContext):
    data = await state.get_data()
    photo_id = message.photo[-1].file_id
    file_url = await get_photo(photo_id)
    if 'fire_alarm_system' in data:
        data['fire_alarm_system'].append(message.photo[-1].file_id)
    else:
        data['fire_alarm_system'] = [message.photo[-1].file_id]
    button_1 = InlineKeyboardButton(
        text='Добавить еще',
        callback_data="add_more_fire_alarm_system"
    )
    button_2 = InlineKeyboardButton(
        text='Закончить',
        callback_data='end_add_fire_alarm_system'
    )
    kb = [[button_1], [button_2]]
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=kb
    )
    await message.answer(text=lexicon['add_more'], reply_markup=keyboard)


async def got_fire_alarm_system(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    button = InlineKeyboardButton(
        text='✅Фото пожарной сигнализации',
        callback_data="done"
    )
    for num in range(len(data['current_keyboard'])):
        if data['current_keyboard'][num][0].callback_data == 'fire_alarm_system':
            data['current_keyboard'][num][0] = button
            break
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=data['current_keyboard']
    )
    await state.update_data(current_keyboard=data['current_keyboard'])
    await callback.message.edit_text(text=lexicon['got_photo'], reply_markup=keyboard)
    await state.set_state(state=None)
