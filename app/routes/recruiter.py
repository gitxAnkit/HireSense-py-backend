from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from app import models, schemas

router = APIRouter(
    prefix="/recruiter",
    tags=["Recruiter"]
)

@router.post("/", response_model=schemas.Recruiter, status_code=status.HTTP_201_CREATED)
def create_recruiter(recruiter: schemas.RecruiterCreate, db: Session = Depends(get_db)):
    """
    Create a new recruiter profile.
    Validates that the company_id and user_id exist.
    """
    # Verify user exists and has recruiter/admin role
    db_user = db.query(models.User).filter(models.User.id == recruiter.user_id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User not found"
        )
    if db_user.role != models.RoleEnum.recruiter and db_user.role != models.RoleEnum.admin:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User does not have recruiter or admin role"
        )
    
    # Verify company exists
    db_company = db.query(models.Company).filter(models.Company.id == recruiter.company_id).first()
    if not db_company:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Company not found"
        )
        
    # Verify recruiter profile doesn't already exist for this user
    db_recruiter = db.query(models.Recruiter).filter(models.Recruiter.user_id == recruiter.user_id).first()
    if db_recruiter:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Recruiter profile already exists for this user"
        )

    new_recruiter = models.Recruiter(
        user_id=recruiter.user_id,
        company_id=recruiter.company_id
    )
    
    db.add(new_recruiter)
    db.commit()
    db.refresh(new_recruiter)
    return new_recruiter

@router.get("/", response_model=List[schemas.Recruiter])
def list_recruiters(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve all recruiters.
    """
    recruiters = db.query(models.Recruiter).offset(skip).limit(limit).all()
    return recruiters

@router.get("/{recruiter_id}", response_model=schemas.Recruiter)
def get_recruiter(recruiter_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single recruiter profile by ID.
    """
    db_recruiter = db.query(models.Recruiter).filter(models.Recruiter.id == recruiter_id).first()
    if not db_recruiter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recruiter profile not found"
        )
    return db_recruiter
