from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.job import Job, JobCreate
from app.services.job_service import job_service

router = APIRouter(
    prefix="/job",
    tags=["Job"]
)

@router.post("/", response_model=Job, status_code=status.HTTP_201_CREATED)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    """
    Create a new job posting.
    Validates that the referenced company_id and created_by (recruiter) exist.
    """
    return job_service.create_job(db, job)

@router.get("/", response_model=List[Job])
def list_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve all job postings with pagination support.
    """
    return job_service.list_jobs(db, skip, limit)

@router.get("/{job_id}", response_model=Job)
def get_job(job_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single job posting by its ID.
    Raises a 404 error if the job does not exist.
    """
    return job_service.get_job(db, job_id)
