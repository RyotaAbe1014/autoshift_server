from sqlalchemy.orm import Session
from typing import Optional, List
from models.shift import Shift as ShiftModel
from schemas.shift import ShiftCreate as ShiftCreateSchema
from schemas.shift import Shift as ShiftSchema
from typing import List
import datetime

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


def get_shifts(db: Session, user_id: int) -> List[ShiftModel]:
    """
    来週のシフトを取得
    """
    print("user_id: ", user_id)
    # 来週の日曜日の日付を取得
    today = datetime.date.today()
    sunday = today + datetime.timedelta(days=6-today.weekday())
    
    # 来週の日曜日から土曜日までの日付を取得
    date_list = []
    for i in range(7):
        date_list.append(sunday + datetime.timedelta(days=i))
    
    # 来週の日曜日から土曜日までのシフトを取得
    shift_list = []
    for date in date_list:
        shift = db.query(ShiftModel).filter(ShiftModel.user_id == user_id, ShiftModel.start_time == date).first()
        if shift:
            shift_list.append(shift)
        else:
            shift_list.append(ShiftModel(user_id=user_id, start_time=date))
    return shift_list


    

