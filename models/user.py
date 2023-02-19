from db import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime


class User(Base):
    """
    ユーザー情報テーブル
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True,  autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone_number = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    organization_id = Column(Integer,ForeignKey('organizations.id', ondelete='CASCADE'), nullable=False)
    organization = relationship("Organization", back_populates="users")
