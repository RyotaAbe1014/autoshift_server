from fastapi import APIRouter, Body, Path, Depends
from typing import Optional, List
from auth.oauth2 import oauth2_scheme, decode_token
from db import session
from settings.custom_route import CustomRoute
from schemas.shift import ShiftCreate, Shift
from cruds.shift import create_shift as crud_create_shift
from cruds.shift import get_shifts as crud_get_shifts
from cruds.shift import get_shifts_target_date as crud_get_shifts_target_date



router = APIRouter(prefix="/shifts", tags=["shifts"], route_class=CustomRoute)


# シフト新規追加
@router.post("/", status_code=201)
async def create_shift(token: str = Depends(oauth2_scheme), shift_create_list: List[ShiftCreate] = Body(...)):
    return crud_create_shift(db=session, shift_create_list=shift_create_list)


# シフト一件追加
@router.post("/{user_id}", status_code=201)
async def create_shift(token: str = Depends(oauth2_scheme), user_id: int = Path(None), shift_create: ShiftCreate = Body(...)):
    return crud_create_shift(db=session, shift_create_list=[shift_create])

# ユーザーシフト一覧取得
@router.get("/{user_id}", status_code=200)
async def get_shifts(token: str = Depends(oauth2_scheme), user_id: int = Path(None)):
    return crud_get_shifts(db=session, user_id=user_id)


# 当日シフト一覧取得
@router.get("/{target_date}", status_code=200)
async def get_shifts(token: str = Depends(oauth2_scheme), target_date: str = Path(None)):
    return crud_get_shifts_target_date(db=session, target_date=target_date)

