from aiogram.fsm.context import FSMContext
from aiogram.types import Message
import utils.db_api.quick_commands as commands

from config.bot_config import bot


async def send_message(message: Message, state: FSMContext):
    data = await state.get_data()
    if 'vehicle_request_id' in data:
        vehicle_request_id = data['vehicle_request_id']
        vehicle_request = await commands.select_vehicle_request(vehicle_request_id)
        user_id = vehicle_request.user_id
    else:
        house_request_id = data['house_request_id']
        house_request = await commands.select_vehicle_request(house_request_id)
        user_id = house_request.user_id
    msg = message.text
    await bot.send_message(chat_id=user_id, text=msg)
