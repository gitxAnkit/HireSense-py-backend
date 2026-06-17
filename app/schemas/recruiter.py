from pydantic import BaseModel

class RecruiterBase(BaseModel):
    company_id: int
    user_id: int

class RecruiterCreate(RecruiterBase):
    pass

class Recruiter(RecruiterBase):
    id: int
    class Config:
        from_attributes = True
