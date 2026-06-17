from typing import Optional
from pydantic import BaseModel

class CompanyBase(BaseModel):
    name: str
    website: Optional[str] = None
    description: Optional[str] = None

class CompanyCreate(CompanyBase):
    pass

class Company(CompanyBase):
    id: int
    class Config:
        from_attributes = True
