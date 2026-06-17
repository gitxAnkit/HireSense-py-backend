from datetime import datetime
from pydantic import BaseModel
from app.models.interview import InterviewStatusEnum

class InterviewBase(BaseModel):
    application_id: int
    round_number: int
    interviewer_id: int
    scheduled_at: datetime
    duration: int
    status: InterviewStatusEnum = InterviewStatusEnum.scheduled

class InterviewCreate(InterviewBase):
    pass

class Interview(InterviewBase):
    id: int
    class Config:
        from_attributes = True
