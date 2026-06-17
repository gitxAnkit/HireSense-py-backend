from sqlalchemy.orm import Session
from app.models.recruiter import Recruiter
from app.schemas.recruiter import RecruiterCreate

class RecruiterRepository:
    def get_by_id(self, db: Session, recruiter_id: int) -> Recruiter:
        return db.query(Recruiter).filter(Recruiter.id == recruiter_id).first()

    def get_by_user_id(self, db: Session, user_id: int) -> Recruiter:
        return db.query(Recruiter).filter(Recruiter.user_id == user_id).first()

    def list(self, db: Session, skip: int = 0, limit: int = 100) -> list[Recruiter]:
        return db.query(Recruiter).offset(skip).limit(limit).all()

    def create(self, db: Session, recruiter: RecruiterCreate) -> Recruiter:
        db_recruiter = Recruiter(
            user_id=recruiter.user_id,
            company_id=recruiter.company_id
        )
        db.add(db_recruiter)
        db.commit()
        db.refresh(db_recruiter)
        return db_recruiter

recruiter_repository = RecruiterRepository()
