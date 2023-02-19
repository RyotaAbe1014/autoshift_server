from db import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime


class Organization(Base):
    """
    企業情報テーブル
    """
    __tablename__ = 'organizations'

    id = Column(Integer, primary_key=True,  autoincrement=True)
    name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    users = relationship("User", back_populates="organization")
