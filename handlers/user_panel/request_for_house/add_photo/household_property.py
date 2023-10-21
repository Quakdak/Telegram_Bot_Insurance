from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from handlers.user_panel.state_request.state_request_house import request_house
from lexicon.lexicon_ru import lexicon
from utils.check_photo import check_photo
from utils.get_photo import get_photo


async def household_property(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=lexicon['household_property'])
    await state.set_state(request_house.wait_household_property)


async def getting_household_property(message: Message, state: FSMContext):
    data = await state.get_data()
    photo_id = message.photo[-1].file_id
    file_url = await get_photo(photo_id)
    check_result = await check_photo(file_url)
    if check_result is True:
        if 'household_property' in data:
            data['household_property'].append(message.photo[-1].file_id)
        else:
            data['household_property'] = [message.photo[-1].file_id]
        button_1 = InlineKeyboardButton(
            text='Добавить еще',
            callback_data="add_more_household_property"
        )
        button_2 = InlineKeyboardButton(
            text='Закончить',
            callback_data='end_add_household_property'
        )
        kb = [[button_1], [button_2]]
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=kb
        )
        await message.answer(text=lexicon['add_more'], reply_markup=keyboard)
    else:
        button = InlineKeyboardButton(text='Отправить еще раз', callback_data="add_more_household_property")
        kb = [[button]]
        keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
        await message.answer(text=check_result, reply_markup=keyboard)


async def got_household_property(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    button = InlineKeyboardButton(
        text='✅Фото домашнего имущества',
        callback_data="done"
    )
    for num in range(len(data['current_keyboard'])):
        if data['current_keyboard'][num][0].callback_data == 'household_property':
            data['current_keyboard'][num][0] = button
            break
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=data['current_keyboard']
    )
    await state.update_data(current_keyboard=data['current_keyboard'])
    await callback.message.edit_text(text=lexicon['got_photo'], reply_markup=keyboard)
    await state.set_state(state=None)
