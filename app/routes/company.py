from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from app import models, schemas

router = APIRouter(
    prefix="/company",
    tags=["Company"]
)

@router.post("/", response_model=schemas.Company, status_code=status.HTTP_201_CREATED)
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    """
    Create a new company.
    """
    # Optional: Check if company name already exists to prevent duplicate entries
    db_company = db.query(models.Company).filter(models.Company.name == company.name).first()
    if db_company:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Company name already registered"
        )
    
    new_company = models.Company(
        name=company.name,
        website=company.website,
        description=company.description
    )
    
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company

@router.get("/", response_model=List[schemas.Company])
def list_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve all companies with optional pagination.
    """
    companies = db.query(models.Company).offset(skip).limit(limit).all()
    return companies

@router.get("/{company_id}", response_model=schemas.Company)
def get_company(company_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single company by ID.
    Raises a 404 error if company does not exist.
    """
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if not db_company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found"
        )
    return db_company
