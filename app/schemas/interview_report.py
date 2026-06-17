from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from app.models.interview_report import RecommendationEnum

class InterviewReportBase(BaseModel):
    interview_id: int
    rating: int
    feedback_text: str
    strengths: Optional[str] = None
    weaknesses: Optional[str] = None
    recommendation: RecommendationEnum

class InterviewReportCreate(InterviewReportBase):
    pass

class InterviewReport(InterviewReportBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True
