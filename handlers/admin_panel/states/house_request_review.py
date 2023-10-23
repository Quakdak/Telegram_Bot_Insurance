from aiogram.fsm.state import State, StatesGroup


class FSMHouseRequestReview(StatesGroup):
    choose_house_request = State()
    process_house_request = State()
    get_house_request_verdict = State()
    write_message_to_user = State()
