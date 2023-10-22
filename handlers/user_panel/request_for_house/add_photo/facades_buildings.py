from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from handlers.user_panel.state_request.state_request_house import request_house
from lexicon.lexicon_ru import lexicon
from utils.check_photo import check_photo
from utils.get_photo import get_photo


async def facades_buildings(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=lexicon['facades_buildings'])
    await state.set_state(request_house.wait_facades_buildings)


async def getting_facades_buildings(message: Message, state: FSMContext):
    data = await state.get_data()
    photo_id = message.document.file_id
    file_url = await get_photo(photo_id)
    check_result = await check_photo(file_url)
    if check_result is True:
        if 'facades_buildings' in data:
            data['facades_buildings'].append(message.document.file_id)
        else:
            data['facades_buildings'] = [message.document.file_id]
        button_1 = InlineKeyboardButton(
            text='Добавить еще',
            callback_data="add_more_facades_buildings"
        )
        button_2 = InlineKeyboardButton(
            text='Закончить',
            callback_data='end_add_facades_buildings'
        )
        kb = [[button_1], [button_2]]
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=kb
        )
        await state.set_data(data)
        await message.answer(text=lexicon['add_more'], reply_markup=keyboard)
    else:
        button = InlineKeyboardButton(text='Отправить еще раз', callback_data="add_more_facades_buildings")
        kb = [[button]]
        keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
        await message.answer(text=check_result, reply_markup=keyboard)


async def got_facades_buildings(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    button = InlineKeyboardButton(
        text='✅Фото фасадов строений',
        callback_data="done"
    )
    for num in range(len(data['current_keyboard'])):
        if data['current_keyboard'][num][0].callback_data == 'facades_buildings':
            data['current_keyboard'][num][0] = button
            break
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=data['current_keyboard']
    )
    await state.update_data(current_keyboard=data['current_keyboard'])
    await callback.message.edit_text(text=lexicon['got_photo'], reply_markup=keyboard)
    await state.set_state(state=None)
