from pydantic import BaseModel
import datetime

class Shift(BaseModel):
    id: int
    start_time: datetime
    end_time: datetime
    user_id: int
    created_at: datetime
    updated_at: datetime


class ShiftCreate(BaseModel):
    start_time: datetime
    end_time: datetime
    user_id: int