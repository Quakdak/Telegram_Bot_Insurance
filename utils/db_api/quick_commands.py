from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db

from utils.db_api.schemas.user import User
from utils.db_api.schemas.vehicle_request import VehicleRequest
from utils.db_api.schemas.house_request import HouseRequest


async def add_user(user_id: int, first_name: str, last_name: str, is_admin: bool):
    try:
        user = User(user_id=user_id, first_name=first_name, last_name=last_name, is_admin=is_admin)
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


async def add_vehicle_request(user_id: int, data: list):
    try:
        vehicle_request = VehicleRequest(user_id=user_id, data=data)
        await vehicle_request.create()
    except UniqueViolationError:
        print('Заявка на транспорт не добавлена')


async def add_house_request(user_id: int, data: list):
    try:
        house_request = HouseRequest(user_id=user_id, data=data)
        await house_request.create()
    except UniqueViolationError:
        print('Заявка на дом не добавлена')


async def select_all_house_requests():
    house_requests = await HouseRequest.query.gino.all()
    return house_requests


async def select_all_vehicle_requests():
    vehicle_requests = await VehicleRequest.query.gino.all()
    return vehicle_requests


async def select_house_request(house_request_id):
    user = await User.query.where(HouseRequest.id == house_request_id).gino.first()
    return user


async def select_vehicle_request(vehicle_request_id):
    user = await User.query.where(VehicleRequest.id == vehicle_request_id).gino.first()
    return user
