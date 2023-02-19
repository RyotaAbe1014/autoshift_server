from fastapi import APIRouter, Body, Path
from typing import List
from db import session
from schemas.organization import OrganizationCreate
from cruds.organization import create_organization as create_organization_crud
from settings.custom_route import CustomRoute
router = APIRouter(prefix="/organization", tags=["organization"], route_class=CustomRoute)


@router.post("/", response_model=OrganizationCreate)
async def create_organization(organization: OrganizationCreate = Body()):
    organization = create_organization_crud(session, organization)
    return organization