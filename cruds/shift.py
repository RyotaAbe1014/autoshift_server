from sqlalchemy.orm import Session
from typing import Optional, List
from models.shift import Shift as ShiftModel
from schemas.shift import ShiftCreate as ShiftCreateSchema
from schemas.shift import Shift as ShiftSchema
from typing import List


def create_shift(db: Session, shift_create_list: List[ShiftCreateSchema]) -> List[ShiftModel]:
    """
    シフト新規追加
    """
    shift_list = []
    for shift_create in shift_create_list:
        shift_list.append(ShiftModel(**shift_create.dict()))
    db.add_all(shift_list)
    db.commit()
    db.refresh_all(shift_list)
    return shift_list