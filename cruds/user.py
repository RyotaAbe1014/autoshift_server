from sqlalchemy.orm import Session
from typing import Optional, List
from models.user import User as UserModel
from schemas.user import UserCreate as UserCreateSchema
from schemas.user import User as UserSchema


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
    users = db.query(UserModel).filter(
        UserModel.organization_id == organization_id).all()
    return users


def get_user(db: Session, organization_id: int, user_id: int) -> UserModel:
    user = db.query(UserModel).filter(
        UserModel.organization_id == organization_id, UserModel.id == user_id).first()
    return user


def delete_user(db: Session, user_id: int) -> None:
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return
    return None


def update_user(db: Session, user_id: int, user_create: UserCreateSchema, organization_id: int) -> UserModel:
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user:
        user.name = user_create.name
        user.email = user_create.email
        user.phone_number = user_create.phone_number
        user.organization_id = organization_id
        db.commit()
        db.refresh(user)
        return user
    return None
    
