from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from handlers.user_panel.state_request.state_request_house import request_house
from lexicon.lexicon_ru import lexicon


async def mechanical_protection(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=lexicon['mechanical_protection'])
    await state.set_state(request_house.wait_defect)


async def getting_mechanical_protection(message: Message, state: FSMContext):
    data = await state.get_data()
    if 'mechanical_protection' in data:
        data['mechanical_protection'].append(message.photo[-1].file_id)
    else:
        data['mechanical_protection'] = [message.photo[-1].file_id]
    button_1 = InlineKeyboardButton(
        text='Добавить еще',
        callback_data="add_more_mechanical_protection"
    )
    button_2 = InlineKeyboardButton(
        text='Закончить',
        callback_data='end_add_mechanical_protection'
    )
    kb = [[button_1], [button_2]]
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=kb
    )
    await message.answer(text=lexicon['add_more'], reply_markup=keyboard)


async def got_mechanical_protection(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    button = InlineKeyboardButton(
        text='✅Фото механической защиты окон и дверей',
        callback_data="done"
    )
    for num in range(len(data['current_keyboard'])):
        if data['current_keyboard'][num][0].callback_data == 'mechanical_protection':
            data['current_keyboard'][num][0] = button
            break
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=data['current_keyboard']
    )
    await state.update_data(current_keyboard=data['current_keyboard'])
    await callback.message.edit_text(text=lexicon['got_photo'], reply_markup=keyboard)
    await state.set_state(state=None)
