from data.config_db import Base
from sqlalchemy import Column, Integer, String, ForeignKey,ARRAY,DateTime
from datetime import datetime

class request_vehicle(Base):
    __tablename__ = 'requests_vehicle'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    data = Column(ARRAY(String), nullable=False)
    date = Column(DateTime, default=datetime.now())
