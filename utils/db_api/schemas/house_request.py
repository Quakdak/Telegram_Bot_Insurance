from sqlalchemy import Column, BigInteger, String, sql, ForeignKey, ARRAY, Sequence, Integer
from sqlalchemy.ext.mutable import MutableList
from utils.db_api.db_gino import TimedBaseModel


class HouseRequest(TimedBaseModel):
    __tablename__ = 'house_requests'
    id = Column(Integer, Sequence('house_request_id_seq'), primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.user_id'), nullable=False)
    data = Column(MutableList.as_mutable(ARRAY(String)))
    status = Column(String, nullable=False, default='pending')

    query: sql.select
