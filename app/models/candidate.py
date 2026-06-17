from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.core.database import Base

candidate_skills = Table(
    "candidate_skills",
    Base.metadata,
    Column("candidate_id", Integer, ForeignKey("candidate_profiles.id"), primary_key=True),
    Column("skill_id", Integer, ForeignKey("skills.id"), primary_key=True)
)

class CandidateProfile(Base):
    __tablename__ = "candidate_profiles"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    resume_url = Column(String)
    experience_years = Column(Integer)
    current_company = Column(String)
    education = Column(String)

    user = relationship("User", back_populates="candidate_profile")
    skills = relationship("Skill", secondary=candidate_skills, back_populates="candidates")
    applications = relationship("Application", back_populates="candidate")
