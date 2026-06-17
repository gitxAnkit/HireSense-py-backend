from datetime import datetime
from pydantic import BaseModel
from app.models.application import AppStatusEnum

class ApplicationBase(BaseModel):
    job_id: int
    candidate_id: int
    status: AppStatusEnum = AppStatusEnum.applied

class ApplicationCreate(ApplicationBase):
    pass

class Application(ApplicationBase):
    id: int
    applied_at: datetime
    updated_at: datetime
    class Config:
        from_attributes = True
