import enum
from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, Enum, DateTime, Text
from sqlalchemy.orm import relationship
from app.core.database import Base

class RecommendationEnum(str, enum.Enum):
    hire = "hire"
    reject = "reject"
    maybe = "maybe"

class InterviewReport(Base):
    __tablename__ = "interview_reports"
    id = Column(Integer, primary_key=True, index=True)
    interview_id = Column(Integer, ForeignKey("interviews.id"))
    rating = Column(Integer)
    feedback_text = Column(Text)
    strengths = Column(Text)
    weaknesses = Column(Text)
    recommendation = Column(Enum(RecommendationEnum))
    created_at = Column(DateTime, default=datetime.utcnow)

    interview = relationship("Interview", back_populates="report")
