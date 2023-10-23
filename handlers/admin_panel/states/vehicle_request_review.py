from aiogram.fsm.state import State, StatesGroup


class FSMVehicleRequestReview(StatesGroup):
    choose_vehicle_request = State()
    process_vehicle_request = State()
    get_vehicle_request_verdict = State()
    write_message_to_user = State()
