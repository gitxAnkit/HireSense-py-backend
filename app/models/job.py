import enum
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime, Table, Text
from sqlalchemy.orm import relationship
from app.core.database import Base

class JobStatusEnum(str, enum.Enum):
    open = "open"
    closed = "closed"
    draft = "draft"

job_skills = Table(
    "job_skills",
    Base.metadata,
    Column("job_id", Integer, ForeignKey("jobs.id"), primary_key=True),
    Column("skill_id", Integer, ForeignKey("skills.id"), primary_key=True)
)

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    description = Column(Text)
    location = Column(String)
    salary_min = Column(Integer)
    salary_max = Column(Integer)
    experience_required = Column(Integer)
    status = Column(Enum(JobStatusEnum), default=JobStatusEnum.draft)
    expiry_date = Column(DateTime)
    created_by = Column(Integer, ForeignKey("recruiters.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    company = relationship("Company", back_populates="jobs")
    creator = relationship("Recruiter", back_populates="jobs")
    skills = relationship("Skill", secondary=job_skills, back_populates="jobs")
    applications = relationship("Application", back_populates="job")
