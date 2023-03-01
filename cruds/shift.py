from sqlalchemy.orm import Session
from typing import Optional, List
from models.shift import Shift as ShiftModel
from models.organization import Organization as OrganizationModel
from models.user import User as UserModel
from schemas.shift import ShiftCreate as ShiftCreateSchema
from schemas.shift import Shift as ShiftSchema
from typing import List
import datetime


def create_shift(db: Session, shift_create_list: List[ShiftCreateSchema]) -> None:
    """
    シフト新規追加
    """
    for shift_create in shift_create_list:
        # 既にシフトが登録されているか確認
        shift = db.query(ShiftModel).filter(
            ShiftModel.user_id == shift_create.user_id, ShiftModel.date == shift_create.date).first()
        print("shift: ", shift)
        if shift:
            # シフトが登録されている場合は更新
            shift.start_time = shift_create.start_time
            shift.end_time = shift_create.end_time
            db.flush()
        else:
            # シフトが登録されていない場合は新規作成
            shift = ShiftModel(user_id=shift_create.user_id, date=shift_create.date,
                               start_time=shift_create.start_time, end_time=shift_create.end_time)
            db.add(shift)
            db.flush()
    db.commit()
    return {"message": "シフトを作成しました"}


def get_shifts(db: Session, user_id: int) -> List[ShiftModel]:
    """
    来週のシフトを取得
    """
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
        shift = db.query(ShiftModel).filter(
            ShiftModel.user_id == user_id, ShiftModel.date == date).first()
        if shift:
            shift_list.append(shift)
        else:
            shift_list.append(ShiftModel(user_id=user_id, date=date))
    return shift_list


# その日のシフトを取得
def get_shifts_target_date(db: Session, organization_id: int, target_date: str) -> List[ShiftModel]:
    """
    検索日のシフトを取得
    """
    # 検索日の日付を取得
    date = datetime.datetime.strptime(target_date, '%Y-%m-%d').date()

    shift_list = db.query(ShiftModel).join(UserModel).filter(
        UserModel.organization_id == organization_id, ShiftModel.date == date).all()
    
    return shift_list