from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.core.database import Base

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    website = Column(String)
    description = Column(Text)

    recruiters = relationship("Recruiter", back_populates="company")
    jobs = relationship("Job", back_populates="company")
