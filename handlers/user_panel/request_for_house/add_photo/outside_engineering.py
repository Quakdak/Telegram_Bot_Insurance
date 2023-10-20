from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from handlers.user_panel.state_request.state_request_house import request_house
from lexicon.lexicon_ru import lexicon


async def outside_engineering(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=lexicon['outside_engineering'])
    await state.set_state(request_house.wait_outside_engineering)


async def getting_outside_engineering(message: Message, state: FSMContext):
    data = await state.get_data()
    if 'outside_engineering' in data:
        data['outside_engineering'].append(message.photo[-1].file_id)
    else:
        data['outside_engineering'] = [message.photo[-1].file_id]
    button_1 = InlineKeyboardButton(
        text='Добавить еще',
        callback_data="add_more_outside_engineering"
    )
    button_2 = InlineKeyboardButton(
        text='Закончить',
        callback_data='end_add_outside_engineering'
    )
    kb = [[button_1], [button_2]]
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=kb
    )
    await message.answer(text=lexicon['add_more'], reply_markup=keyboard)


async def got_outside_engineering(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    button = InlineKeyboardButton(
        text='✅Фото наружных инженерных коммуникаций',
        callback_data="done"
    )
    for num in range(len(data['current_keyboard'])):
        if data['current_keyboard'][num][0].callback_data == 'outside_engineering':
            data['current_keyboard'][num][0] = button
            break
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=data['current_keyboard']
    )
    await state.update_data(current_keyboard=data['current_keyboard'])
    await callback.message.edit_text(text=lexicon['got_photo'], reply_markup=keyboard)
    await state.set_state(state=None)
