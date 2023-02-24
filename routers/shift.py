from fastapi import APIRouter, Body, Path, Depends
from typing import Optional, List
from auth.oauth2 import oauth2_scheme, decode_token
from db import session
from settings.custom_route import CustomRoute
from schemas.shift import ShiftCreate, Shift
from cruds.shift import create_shift as crud_create_shift

router = APIRouter(prefix="/shifts", tags=["shifts"], route_class=CustomRoute)


# シフト新規追加
@router.post("/", status_code=201, response_model=List[Shift])
async def create_shift(token: str = Depends(oauth2_scheme), shift_create_list: List[ShiftCreate] = Body(...)):
    return crud_create_shift(db=session, shift_create_list=shift_create_list)