from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Shift(BaseModel):
    id: Optional[int]
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    user_id: int


class ShiftCreate(BaseModel):
    start_time: datetime
    end_time: datetime
    user_id: int


