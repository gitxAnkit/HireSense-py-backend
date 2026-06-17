from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.company_repository import company_repository
from app.schemas.company import CompanyCreate
from app.models.company import Company

class CompanyService:
    def create_company(self, db: Session, company: CompanyCreate) -> Company:
        db_company = company_repository.get_by_name(db, company.name)
        if db_company:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Company name already registered"
            )
        return company_repository.create(db, company)

    def list_companies(self, db: Session, skip: int = 0, limit: int = 100) -> list[Company]:
        return company_repository.list(db, skip, limit)

    def get_company(self, db: Session, company_id: int) -> Company:
        db_company = company_repository.get_by_id(db, company_id)
        if not db_company:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Company not found"
            )
        return db_company

company_service = CompanyService()
