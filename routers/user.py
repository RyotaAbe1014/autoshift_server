from fastapi import APIRouter, Body, Path, Depends
from auth.oauth2 import oauth2_scheme, decode_token
from db import session
from settings.custom_route import CustomRoute
from schemas.user import UserCreate, User
from cruds.user import create_user as crud_create_user
from cruds.organization import get_organization_id



router = APIRouter(prefix="/users", tags=["users"], route_class=CustomRoute)


# ユーザー新規追加
@router.post("/", status_code=201, response_model=User)
async def create_user(token: str = Depends(oauth2_scheme), user_create: UserCreate = Body(...)):
    print("token: ", token)
    decoded_token = decode_token(token)
    organization_id = get_organization_id(db=session, organization_name=decoded_token["sub"])
    return crud_create_user(db=session, user_create=user_create, organization_id=organization_id)
