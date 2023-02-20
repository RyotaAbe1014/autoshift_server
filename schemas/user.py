from pydantic import BaseModel, Field
from typing import Optional


class UserCreate(BaseModel):
    name: str = Field(..., example="テスト太郎")
    email: str = Field(..., example="")
    phone_number: str = Field(..., example="08012345678")


class User(UserCreate):
    id: int = Field(..., example=1)
    organization_id: int = Field(..., example=1)

    class Config:
        orm_mode = True