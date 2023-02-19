from pydantic import BaseModel, Field
from typing import Optional


class OrganizationCreate(BaseModel):
    name: str = Field(..., example="株式会社テスト")
    password: str = Field(..., example="password")

    class Config:
      orm_mode = True