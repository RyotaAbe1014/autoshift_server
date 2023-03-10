from db import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Date, Time
from sqlalchemy.orm import relationship
import datetime


class Shift(Base):
    __tablename__ = 'shifts'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    start_time = Column(Time)
    end_time = Column(Time)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = relationship("User", back_populates="shifts")
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    