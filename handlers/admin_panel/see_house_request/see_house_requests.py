from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InputMediaDocument
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton, InlineKeyboardBuilder

from handlers.admin_panel.see_house_request.hr_callback_factory import HrCallbackFactory
import utils.db_api.quick_commands as commands
from lexicon.lexicon_ru import lexicon


def process_key(key):
    return lexicon[key].replace('Отправьте ', '').replace('(файлом, без сжатия)',
                                                          '').capitalize()


async def see_house_requests(callback: CallbackQuery):
    house_requests = (await commands.select_all_house_requests())[:100]
    callback_data_and_text = [[HrCallbackFactory(house_request_id=i.id), f'Заявка {i.id}'] for i in house_requests]
    if house_requests:
        builder = InlineKeyboardBuilder()
        builder.adjust(3)
        for callback_data, text in callback_data_and_text:
            builder.button(text=text, callback_data=callback_data)
        builder.row(InlineKeyboardButton(text='Назад', callback_data='back_to_admin_panel'))

        await callback.message.edit_text(text='Список заявок на осмотр дома', reply_markup=builder.as_markup())

    else:
        button = InlineKeyboardButton(
            text='Назад',
            callback_data='back_to_admin_panel'
        )
        inline_kb = [[button]]
        keyboard = InlineKeyboardMarkup(inline_keyboard=inline_kb)
        await callback.message.edit_text(text='Список заявок на осмотр дома пуст', reply_markup=keyboard)


async def process_house_request_press(callback: CallbackQuery,
                                      callback_data: HrCallbackFactory, state: FSMContext):
    data = callback_data.pack().split(':')
    house_request_id = int(data[-1])
    await state.update_data(vehicle_request_id=house_request_id)
    house_request = await commands.select_vehicle_request(house_request_id)

    photos_dict = {
        process_key('general_view_house'): house_request.general_view_house,
        process_key('outside_engineering'): house_request.outside_engineering,
        process_key('facades_buildings'): house_request.facades_buildings,
        process_key('mechanical_protection'): house_request.mechanical_protection,
        process_key('front_door'): house_request.front_door,
        process_key('inside_engineering'): house_request.inside_engineering,
        process_key('fire_alarm_system'): house_request.fire_alarm_system,
        process_key('security_alarm_system'): house_request.security_alarm_system,
        process_key('interior'): house_request.interior,
        process_key('window'): house_request.window,
        process_key('defect'): house_request.defect,
        process_key('household_property'): house_request.household_property,
        process_key('fence'): house_request.fence,
        process_key('end_inspection_house'): house_request.end_inspection_house
    }

    for text, photo_ids in photos_dict.items():
        await callback.message.answer(text=text)
        photo_group = []
        for photo_id in photo_ids:
            # await callback.message.answer_document(document=photo_id)
            photo_group.append(InputMediaDocument(media=photo_id))
        await callback.message.answer_media_group(photo_group)

    button_1 = InlineKeyboardButton(
        text='Принять заявку ✅',
        callback_data='accept_vehicle_request'
    )
    button_2 = InlineKeyboardButton(
        text='Отправить на редактирование ➡️',
        callback_data='return_house_request'
    )

    inline_kb = [[button_1], [button_2]]

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=inline_kb
    )

    await callback.message.answer(text='Выберете действие', reply_markup=keyboard)
