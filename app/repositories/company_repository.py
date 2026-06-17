from sqlalchemy.orm import Session
from app.models.company import Company
from app.schemas.company import CompanyCreate

class CompanyRepository:
    def get_by_id(self, db: Session, company_id: int) -> Company:
        return db.query(Company).filter(Company.id == company_id).first()

    def get_by_name(self, db: Session, name: str) -> Company:
        return db.query(Company).filter(Company.name == name).first()

    def list(self, db: Session, skip: int = 0, limit: int = 100) -> list[Company]:
        return db.query(Company).offset(skip).limit(limit).all()

    def create(self, db: Session, company: CompanyCreate) -> Company:
        db_company = Company(
            name=company.name,
            website=company.website,
            description=company.description
        )
        db.add(db_company)
        db.commit()
        db.refresh(db_company)
        return db_company

company_repository = CompanyRepository()
