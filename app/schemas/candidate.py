from typing import List, Optional
from pydantic import BaseModel
from app.schemas.skill import Skill

class CandidateProfileBase(BaseModel):
    resume_url: Optional[str] = None
    experience_years: Optional[int] = None
    current_company: Optional[str] = None
    education: Optional[str] = None

class CandidateProfileCreate(CandidateProfileBase):
    user_id: int

class CandidateProfile(CandidateProfileBase):
    id: int
    user_id: int
    skills: List[Skill] = []
    class Config:
        from_attributes = True
