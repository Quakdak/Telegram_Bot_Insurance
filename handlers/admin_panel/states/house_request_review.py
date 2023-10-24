from aiogram.fsm.state import State, StatesGroup


class FSMHouseRequestReview(StatesGroup):
    write_message_to_user = State()
