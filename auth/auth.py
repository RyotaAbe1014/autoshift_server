from fastapi import APIRouter, HTTPException, status
from fastapi.param_functions import Depends
from fastapi.param_functions import Body
from sqlalchemy.orm.session import Session
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Union
from db import get_db
from models.organization import Organization
from .hash import Hash
from auth import oauth2

router = APIRouter(
    tags=['authentication']
)


class OAuth2PasswordRequestCustomForm(BaseModel):
    name: str
    password: str


@router.post('/token')
def get_token(request: OAuth2PasswordRequestCustomForm = Body(), db: Session = Depends(get_db)):
    print(request)
    organization = db.query(Organization).filter(
        Organization.name == request.name).first()
    if not organization:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Invalid credentials'
        )
    if not Hash.verify_password(organization.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Incorrect password'
        )
    access_token = oauth2.create_access_token(data={'sub': organization.name})
    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'organization_id': organization.id,
        'organization_name': organization.name
    }
