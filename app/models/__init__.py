from app.core.database import Base
from app.models.user import User, RoleEnum
from app.models.candidate import CandidateProfile, candidate_skills
from app.models.company import Company
from app.models.recruiter import Recruiter
from app.models.job import Job, JobStatusEnum, job_skills
from app.models.skill import Skill
from app.models.application import Application, AppStatusEnum
from app.models.interview import Interview, InterviewStatusEnum
from app.models.interview_report import InterviewReport, RecommendationEnum
