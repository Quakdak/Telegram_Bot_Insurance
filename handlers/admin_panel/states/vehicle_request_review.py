from aiogram.fsm.state import State, StatesGroup


class FSMVehicleRequestReview(StatesGroup):
    write_message_to_user = State()
