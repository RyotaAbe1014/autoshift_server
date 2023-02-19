from fastapi import APIRouter, HTTPException, status
from fastapi.param_functions import Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from db import get_db
from models.organization import Organization
from .hash import Hash
from auth import oauth2

router = APIRouter(
    tags=['authentication']
)

@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    organization = db.query(Organization).filter(
        Organization.name == request.username).first()
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
