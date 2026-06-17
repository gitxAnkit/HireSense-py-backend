from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.recruiter import Recruiter, RecruiterCreate
from app.services.recruiter_service import recruiter_service

router = APIRouter(
    prefix="/recruiter",
    tags=["Recruiter"]
)

@router.post("/", response_model=Recruiter, status_code=status.HTTP_201_CREATED)
def create_recruiter(recruiter: RecruiterCreate, db: Session = Depends(get_db)):
    """
    Create a new recruiter profile.
    Validates that the company_id and user_id exist.
    """
    return recruiter_service.create_recruiter(db, recruiter)

@router.get("/", response_model=List[Recruiter])
def list_recruiters(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve all recruiters.
    """
    return recruiter_service.list_recruiters(db, skip, limit)

@router.get("/{recruiter_id}", response_model=Recruiter)
def get_recruiter(recruiter_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single recruiter profile by ID.
    """
    return recruiter_service.get_recruiter(db, recruiter_id)
