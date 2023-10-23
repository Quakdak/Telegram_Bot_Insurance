from sqlalchemy import Column, BigInteger, String, sql, ForeignKey, ARRAY, Integer, Sequence
from utils.db_api.db_gino import TimedBaseModel


class VehicleRequest(TimedBaseModel):
    __tablename__ = 'vehicle_requests'
    id = Column(Integer, Sequence('vehicle_request_id_seq'), primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.user_id'), nullable=False)
    damage = Column(ARRAY(String), default=[])
    key = Column(ARRAY(String), nullable=False)
    mark_windshield = Column(ARRAY(String), nullable=False)
    odometer = Column(ARRAY(String), nullable=False)
    transport_outside = Column(ARRAY(String), nullable=False)
    transport_inside = Column(ARRAY(String), nullable=False)
    vin_number = Column(ARRAY(String), nullable=False)
    wheel = Column(ARRAY(String), nullable=False)
    windshield = Column(ARRAY(String), nullable=False)
    status = Column(String, nullable=False, default='pending')

    query: sql.select
