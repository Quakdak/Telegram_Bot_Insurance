from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InputMediaDocument
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton, InlineKeyboardBuilder
import utils.db_api.quick_commands as commands
from .vr_callback_factory import VrCallbackFactory
from lexicon.lexicon_ru import lexicon


def process_key(key):
    return lexicon[key].replace('Отправьте ', '').replace('(файлом, без сжатия)',
                                                          '').capitalize()


async def see_vehicle_requests(callback: CallbackQuery):
    vehicle_requests = await commands.select_all_pending_vehicle_requests()
    if vehicle_requests:
        callback_data_and_text = [[VrCallbackFactory(vehicle_request_id=i.id), f'Заявка {i.id}'] for i in
                                  vehicle_requests[:100]]
        builder = InlineKeyboardBuilder()
        builder.adjust(3)
        for callback_data, text in callback_data_and_text:
            builder.button(text=text, callback_data=callback_data)
        builder.row(InlineKeyboardButton(text='Назад', callback_data='back_to_admin_panel'))

        await callback.message.edit_text(text='Список заявок на осмотр транспорта', reply_markup=builder.as_markup())
    else:
        button = InlineKeyboardButton(
            text='Назад',
            callback_data='back_to_admin_panel'
        )
        inline_kb = [[button]]
        keyboard = InlineKeyboardMarkup(inline_keyboard=inline_kb)
        await callback.message.edit_text(text='Список заявок на осмотр транспорта пуст', reply_markup=keyboard)


async def process_vehicle_request_press(callback: CallbackQuery,
                                        callback_data: VrCallbackFactory, state: FSMContext):
    data = callback_data.pack().split(':')
    vehicle_request_id = int(data[-1])
    await state.update_data(vehicle_request_id=vehicle_request_id)
    vehicle_request = await commands.select_vehicle_request(vehicle_request_id)

    photos_dict = {
        process_key('damage'): vehicle_request.damage,
        process_key('key'): vehicle_request.key,
        process_key('mark_windshield'): vehicle_request.mark_windshield,
        process_key('odometer'): vehicle_request.odometer,
        process_key('transport_outside'): vehicle_request.transport_outside,
        process_key('transport_inside'): vehicle_request.transport_inside,
        process_key('vin_number'): vehicle_request.vin_number,
        process_key('wheel'): vehicle_request.wheel,
        process_key('windshield'): vehicle_request.windshield,
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
        callback_data='return_vehicle_request'
    )

    inline_kb = [[button_1], [button_2]]

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=inline_kb
    )

    await callback.message.answer(text='Выберете действие', reply_markup=keyboard)
