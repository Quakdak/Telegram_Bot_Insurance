from sqlalchemy import Column, BigInteger, String, sql, ForeignKey, ARRAY, Sequence, Integer
from utils.db_api.db_gino import TimedBaseModel


class HouseRequest(TimedBaseModel):
    __tablename__ = 'house_requests'
    id = Column(Integer, Sequence('house_request_id_seq'), primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.user_id'), nullable=False)
    defect = Column(ARRAY(String), default=[])
    facades_buildings = Column(ARRAY(String), nullable=False)
    fence = Column(ARRAY(String), nullable=False)
    fire_alarm_system = Column(ARRAY(String), nullable=False)
    front_door = Column(ARRAY(String), nullable=False)
    general_view_house = Column(ARRAY(String), nullable=False)
    household_property = Column(ARRAY(String), nullable=False)
    inside_engineering = Column(ARRAY(String), nullable=False)
    interior = Column(ARRAY(String), nullable=False)
    mechanical_protection = Column(ARRAY(String), nullable=False)
    outside_engineering = Column(ARRAY(String), nullable=False)
    security_alarm_system = Column(ARRAY(String), nullable=False)
    window = Column(ARRAY(String), nullable=False)
    for_edit=Column(ARRAY(String))
    status = Column(String, nullable=False, default='pending')

    query: sql.select
