from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db

from utils.db_api.schemas.user import User
from utils.db_api.schemas.vehicle_request import VehicleRequest
from utils.db_api.schemas.house_request import HouseRequest


async def add_user(user_id: int, first_name: str, last_name: str, username: str, is_admin: bool):
    try:
        user = User(user_id=user_id, first_name=first_name, last_name=last_name, username=username, is_admin=is_admin)
        await user.create()
    except UniqueViolationError:
        print('Пользователь не добавлен')


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def count_users():
    count = await db.func.count(User.user_id).gino.scalar()
    return count


async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user


async def add_house_request(user_id: int, front_door: list, facades_buildings: list, fence: list,
                            fire_alarm_system: list, general_view_house: list, household_property: list,
                            inside_engineering: list, interior: list, mechanical_protection: list,
                            outside_engineering: list, security_alarm_system: list, window: list, defect: list):
    try:
        house_request = HouseRequest(user_id=user_id, defect=defect,
                                     facades_buildings=facades_buildings,
                                     fence=fence,
                                     fire_alarm_system=fire_alarm_system,
                                     front_door=front_door,
                                     general_view_house=general_view_house,
                                     household_property=household_property,
                                     inside_engineering=inside_engineering,
                                     interior=interior,
                                     mechanical_protection=mechanical_protection,
                                     outside_engineering=outside_engineering,
                                     security_alarm_system=security_alarm_system,
                                     window=window)
        await house_request.create()
    except UniqueViolationError:
        print('Заявка на транспорт не добавлена')


async def add_vehicle_request(user_id: int, key: list, mark_windshield: list, odometer: list, transport_inside: list,
                              transport_outside: list, vin_number: list, wheel: list, windshield: list, damage: list):
    try:
        vehicle_request = VehicleRequest(user_id=user_id, damage=damage,
                                         key=key,
                                         mark_windshield=mark_windshield,
                                         odometer=odometer,
                                         transport_outside=transport_outside,
                                         transport_inside=transport_inside,
                                         vin_number=vin_number,
                                         wheel=wheel,
                                         windshield=windshield)
        await vehicle_request.create()
    except UniqueViolationError:
        print('Заявка на дом не добавлена')


async def select_all_house_requests():
    house_requests = await HouseRequest.query.gino.all()
    return house_requests


async def select_all_vehicle_requests():
    vehicle_requests = await VehicleRequest.query.gino.all()
    return vehicle_requests


async def select_all_pending_vehicle_requests():
    vehicle_requests = await VehicleRequest.query.where(
        VehicleRequest.status == 'pending').gino.all()
    return vehicle_requests


async def select_all_pending_house_requests():
    house_requests = await HouseRequest.query.where(
        HouseRequest.status == 'pending').gino.all()
    return house_requests


async def select_house_request(house_request_id):
    house_request = await HouseRequest.query.where(HouseRequest.id == house_request_id).gino.first()
    return house_request


async def select_vehicle_request(vehicle_request_id):
    vehicle_request = await VehicleRequest.query.where(VehicleRequest.id == vehicle_request_id).gino.first()
    return vehicle_request
