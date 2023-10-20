from aiogram.fsm.state import StatesGroup, State


class request_house(StatesGroup):
    wait_general_view_house = State()
    wait_outside_engineering = State()
    wait_facades_buildings = State()
    wait_mechanical_protection = State()
    wait_front_door = State()
    wait_inside_engineering = State()
    wait_fire_alarm_system = State()
    wait_security_alarm_system = State()
    wait_interior = State()
    wait_window = State()
    wait_defect = State()
    wait_household_property = State()
    wait_fence = State()