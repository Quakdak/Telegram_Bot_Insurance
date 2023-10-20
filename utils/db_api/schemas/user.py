from sqlalchemy import Column, BigInteger, String, sql, Boolean

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=True)
    is_admin = Column(Boolean, nullable=False)

    query: sql.select
