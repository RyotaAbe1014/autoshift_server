from fastapi import APIRouter, Body, Path, Depends
from auth.oauth2 import oauth2_scheme, decode_token
from typing import List
from db import session
from schemas.organization import OrganizationCreate, Organization
from cruds.organization import create_organization as create_organization_crud
from cruds.organization import get_organization_id as create_organization_crud
from settings.custom_route import CustomRoute


router = APIRouter(prefix="/organization", tags=["organization"], route_class=CustomRoute)


@router.post("/", response_model=OrganizationCreate)
async def create_organization(organization: OrganizationCreate = Body()):
    organization = create_organization_crud(session, organization)
    return organization


# 会社情報取得
# @router.get("/", response_model=Organization)
# async def get_organization(token: str = Depends(oauth2_scheme)):
#     authorization_data = decode_token(token)
#     organization_id: int = authorization_data["organization_id"]

#     return organization

