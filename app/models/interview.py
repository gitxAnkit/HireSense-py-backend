import enum
from sqlalchemy import Column, Integer, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base

class InterviewStatusEnum(str, enum.Enum):
    scheduled = "scheduled"
    completed = "completed"
    cancelled = "cancelled"

class Interview(Base):
    __tablename__ = "interviews"
    id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, ForeignKey("applications.id"))
    round_number = Column(Integer)
    interviewer_id = Column(Integer, ForeignKey("users.id"))
    scheduled_at = Column(DateTime)
    duration = Column(Integer) # in minutes
    status = Column(Enum(InterviewStatusEnum), default=InterviewStatusEnum.scheduled)

    application = relationship("Application", back_populates="interviews")
    interviewer = relationship("User")
    report = relationship("InterviewReport", back_populates="interview", uselist=False)
