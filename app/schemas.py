from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
import enum

class RoleEnum(str, enum.Enum):
    candidate = "candidate"
    recruiter = "recruiter"
    admin = "admin"

class JobStatusEnum(str, enum.Enum):
    open = "open"
    closed = "closed"
    draft = "draft"

class AppStatusEnum(str, enum.Enum):
    applied = "applied"
    shortlisted = "shortlisted"
    rejected = "rejected"
    hired = "hired"

class InterviewStatusEnum(str, enum.Enum):
    scheduled = "scheduled"
    completed = "completed"
    cancelled = "cancelled"

class RecommendationEnum(str, enum.Enum):
    hire = "hire"
    reject = "reject"
    maybe = "maybe"

# --- Skill ---
class SkillBase(BaseModel):
    name: str

class SkillCreate(SkillBase):
    pass

class Skill(SkillBase):
    id: int
    class Config:
        from_attributes = True

# --- User ---
class UserBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    role: RoleEnum

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

# --- CandidateProfile ---
class CandidateProfileBase(BaseModel):
    resume_url: Optional[str] = None
    experience_years: Optional[int] = None
    current_company: Optional[str] = None
    education: Optional[str] = None

class CandidateProfileCreate(CandidateProfileBase):
    user_id: int

class CandidateProfile(CandidateProfileBase):
    id: int
    user_id: int
    skills: List[Skill] = []
    class Config:
        from_attributes = True

# --- Company ---
class CompanyBase(BaseModel):
    name: str
    website: Optional[str] = None
    description: Optional[str] = None

class CompanyCreate(CompanyBase):
    pass

class Company(CompanyBase):
    id: int
    class Config:
        from_attributes = True

# --- Recruiter ---
class RecruiterBase(BaseModel):
    company_id: int
    user_id: int

class RecruiterCreate(RecruiterBase):
    pass

class Recruiter(RecruiterBase):
    id: int
    class Config:
        from_attributes = True

# --- Job ---
class JobBase(BaseModel):
    title: str
    description: str
    location: str
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    experience_required: Optional[int] = None
    status: JobStatusEnum = JobStatusEnum.draft
    expiry_date: Optional[datetime] = None

class JobCreate(JobBase):
    company_id: int
    created_by: int

class Job(JobBase):
    id: int
    company_id: int
    created_by: int
    created_at: datetime
    skills: List[Skill] = []
    class Config:
        from_attributes = True

# --- Application ---
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

# --- Interview ---
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

# --- InterviewReport ---
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
