from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.job import job_skills
from app.models.candidate import candidate_skills

class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    jobs = relationship("Job", secondary=job_skills, back_populates="skills")
    candidates = relationship("CandidateProfile", secondary=candidate_skills, back_populates="skills")
