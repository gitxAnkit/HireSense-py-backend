import enum
from datetime import datetime
from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base

class RoleEnum(str, enum.Enum):
    candidate = "candidate"
    recruiter = "recruiter"
    admin = "admin"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    password_hash = Column(String)
    role = Column(Enum(RoleEnum))
    created_at = Column(DateTime, default=datetime.utcnow)

    candidate_profile = relationship("CandidateProfile", back_populates="user", uselist=False)
    recruiter_profile = relationship("Recruiter", back_populates="user", uselist=False)
