from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.company import Company, CompanyCreate
from app.services.company_service import company_service

router = APIRouter(
    prefix="/company",
    tags=["Company"]
)

@router.post("/", response_model=Company, status_code=status.HTTP_201_CREATED)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    """
    Create a new company.
    """
    return company_service.create_company(db, company)

@router.get("/", response_model=List[Company])
def list_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve all companies with optional pagination.
    """
    return company_service.list_companies(db, skip, limit)

@router.get("/{company_id}", response_model=Company)
def get_company(company_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single company by ID.
    Raises a 404 error if company does not exist.
    """
    return company_service.get_company(db, company_id)
