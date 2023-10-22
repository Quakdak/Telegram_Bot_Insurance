from aiogram.fsm.state import StatesGroup, State


class request_transport(StatesGroup):
    wait_vin_number = State()
    wait_transport_outside = State()
    wait_windshield = State()
    wait_mark_windshield = State()
    wait_wheel = State()
    wait_odometer = State()
    wait_transport_inside = State()
    wait_damage = State()
    wait_key = State()
