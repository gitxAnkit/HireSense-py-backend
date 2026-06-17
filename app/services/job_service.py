from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.job_repository import job_repository
from app.repositories.company_repository import company_repository
from app.repositories.recruiter_repository import recruiter_repository
from app.schemas.job import JobCreate
from app.models.job import Job

class JobService:
    def create_job(self, db: Session, job: JobCreate) -> Job:
        # Verify company exists
        db_company = company_repository.get_by_id(db, job.company_id)
        if not db_company:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Company not found"
            )
        
        # Verify recruiter exists
        db_recruiter = recruiter_repository.get_by_id(db, job.created_by)
        if not db_recruiter:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Recruiter not found"
            )
        
        return job_repository.create(db, job)

    def list_jobs(self, db: Session, skip: int = 0, limit: int = 100) -> list[Job]:
        return job_repository.list(db, skip, limit)

    def get_job(self, db: Session, job_id: int) -> Job:
        db_job = job_repository.get_by_id(db, job_id)
        if not db_job:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Job not found"
            )
        return db_job

job_service = JobService()
