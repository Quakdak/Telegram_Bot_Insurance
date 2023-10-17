from data.request_house import request_house
from data.request_vehicle import request_vehicle
from data.user import user
from data.config_db import engine, Base, MetaData

Base.metadata.create_all(engine)