from sqlalchemy import Column, BigInteger, String, sql, ForeignKey, ARRAY, Integer, Sequence
from sqlalchemy.ext.mutable import MutableList
from utils.db_api.db_gino import TimedBaseModel


class VehicleRequest(TimedBaseModel):
    __tablename__ = 'vehicle_requests'
    id = Column(Integer, Sequence('vehicle_request_id_seq'), primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.user_id'), nullable=False)
    data = Column(MutableList.as_mutable(ARRAY(String)))
    status = Column(String, nullable=False, default='pending')

    query: sql.select
