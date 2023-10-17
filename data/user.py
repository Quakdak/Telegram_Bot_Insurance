from data.config_db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean

class user(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_first_name = Column(String, nullable=False)
    is_admin = Column(Boolean, nullable=False)
    requests_vehicle = relationship('request_vehicle')
    requests_house = relationship('request_house')
