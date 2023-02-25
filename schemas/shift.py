from pydantic import BaseModel
import datetime
from typing import Optional


class Shift(BaseModel):
    id: Optional[int]
    date: Optional[datetime.date]
    start_time: Optional[datetime.time]
    end_time: Optional[datetime.time]
    user_id: int


class ShiftCreate(BaseModel):
    date: Optional[datetime.date]
    start_time: Optional[datetime.time]
    end_time: Optional[datetime.time]
    user_id: int
