from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from app import models, schemas

router = APIRouter(
    prefix="/job",
    tags=["Job"]
)

@router.post("/", response_model=schemas.Job, status_code=status.HTTP_201_CREATED)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
    """
    Create a new job posting.
    Validates that the referenced company_id and created_by (recruiter) exist.
    """
    # Verify company exists
    db_company = db.query(models.Company).filter(models.Company.id == job.company_id).first()
    if not db_company:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Company not found"
        )
    
    # Verify recruiter exists
    db_recruiter = db.query(models.Recruiter).filter(models.Recruiter.id == job.created_by).first()
    if not db_recruiter:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Recruiter not found"
        )
    
    new_job = models.Job(**job.model_dump())
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job

@router.get("/", response_model=List[schemas.Job])
def list_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve all job postings with pagination support.
    """
    jobs = db.query(models.Job).offset(skip).limit(limit).all()
    return jobs

@router.get("/{job_id}", response_model=schemas.Job)
def get_job(job_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single job posting by its ID.
    Raises a 404 error if the job does not exist.
    """
    db_job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if not db_job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found"
        )
    return db_job

