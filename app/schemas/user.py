from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from app.models.user import RoleEnum

class UserBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    role: RoleEnum

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True
