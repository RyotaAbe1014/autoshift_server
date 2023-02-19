from db import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
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
    business_hours = relationship(
        "OrganizationBusinessHours", back_populates="organization")
    exception_days = relationship(
        "OrganizationExceptionDays", back_populates="organization")


class OrganizationBusinessHours(Base):
    """
    企業の営業時間テーブル
    """
    __tablename__ = 'organization_business_hours'

    id = Column(Integer, primary_key=True,  autoincrement=True)
    organization_id = Column(Integer, ForeignKey(
        'organizations.id', ondelete='CASCADE'), nullable=False)
    day_of_week = Column(Integer, nullable=False)
    start_time = Column(String(255), nullable=False)
    end_time = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    organization = relationship(
        "Organization", back_populates="business_hours")


class OrganizationExceptionDays(Base):
    """
    企業の例外日テーブル
    """
    __tablename__ = 'organization_exception_days'

    id = Column(Integer, primary_key=True,  autoincrement=True)
    organization_id = Column(Integer, ForeignKey(
        'organizations.id', ondelete='CASCADE'), nullable=False)
    date = Column(DateTime, nullable=False)
    exception_type = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    organization = relationship(
        "Organization", back_populates="exception_days")
