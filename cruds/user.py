from sqlalchemy.orm import Session
from typing import Optional, List
from models.user import User as UserModel
from  schemas.user import UserCreate as UserCreateSchema
from  schemas.user import User as UserSchema


def create_user(db: Session, user_create: UserCreateSchema, organization_id: int) -> UserModel:
    user = UserModel(
        name=user_create.name,
        email=user_create.email,
        phone_number=user_create.phone_number,
        organization_id=organization_id
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_users(db: Session, organization_id: int) -> Optional[List[UserSchema]]:
    users = db.query(UserModel).filter(UserModel.organization_id == organization_id).all()
    return users