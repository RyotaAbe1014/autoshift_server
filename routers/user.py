from fastapi import APIRouter, Body, Path
from typing import List
import schemas.user as UserSchema
import cruds.user as crud
from db import session
from settings.custom_route import CustomRoute
router = APIRouter(prefix="/users", tags=["users"], route_class=CustomRoute)


@router.post("/", response_model=UserSchema.UserCreate)
async def create_user(user: UserSchema.UserCreate):
    return crud.create_user(session, user)
