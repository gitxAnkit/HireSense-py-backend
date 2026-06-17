from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from app.models.job import JobStatusEnum
from app.schemas.skill import Skill

class JobBase(BaseModel):
    title: str
    description: str
    location: str
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    experience_required: Optional[int] = None
    status: JobStatusEnum = JobStatusEnum.draft
    expiry_date: Optional[datetime] = None

class JobCreate(JobBase):
    company_id: int
    created_by: int

class Job(JobBase):
    id: int
    company_id: int
    created_by: int
    created_at: datetime
    updated_at: datetime
    skills: List[Skill] = []
    class Config:
        from_attributes = True
