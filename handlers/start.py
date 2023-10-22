from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from lexicon.lexicon_ru import lexicon
import utils.db_api.quick_commands as commands


async def start(message: Message, state: FSMContext):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    await state.update_data(user_id=user_id)

    user = await commands.select_user(user_id)
    if not user:
        await commands.add_user(user_id=user_id, first_name=user_name,
                                last_name=message.from_user.last_name, is_admin=False)
        user = await commands.select_user(user_id)

    button_1 = InlineKeyboardButton(
        text='Подать заявку',
        callback_data='apply_request'
    )
    button_2 = InlineKeyboardButton(
        text='Активные заявки',
        callback_data='active_requests'
    )
    button_3 = InlineKeyboardButton(
        text='Принятые заявки',
        callback_data='applied_requests'
    )
    inline_kb = [[button_1], [button_2], [button_3]]
    if user.is_admin:
        button4 = InlineKeyboardButton(
            text='Админ панель',
            callback_data='admin_panel'
        )
        inline_kb.append([button4])

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=inline_kb
    )
    await state.update_data(current_keyboard=inline_kb)
    await message.answer(lexicon["start"].format(user_name),
                         reply_markup=keyboard)
