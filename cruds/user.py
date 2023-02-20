from sqlalchemy.orm import Session
from models.user import User as UserModel
import schemas.user as UserCreate


def create_user(db: Session, user_create: UserCreate, organization_id: int) -> UserModel:
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
