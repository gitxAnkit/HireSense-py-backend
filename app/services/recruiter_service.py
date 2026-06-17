from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.recruiter_repository import recruiter_repository
from app.repositories.user_repository import user_repository
from app.repositories.company_repository import company_repository
from app.schemas.recruiter import RecruiterCreate
from app.models.recruiter import Recruiter
from app.models.user import RoleEnum

class RecruiterService:
    def create_recruiter(self, db: Session, recruiter: RecruiterCreate) -> Recruiter:
        # Verify user exists and has recruiter/admin role
        db_user = user_repository.get_by_id(db, recruiter.user_id)
        if not db_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User not found"
            )
        if db_user.role != RoleEnum.recruiter and db_user.role != RoleEnum.admin:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User does not have recruiter or admin role"
            )
        
        # Verify company exists
        db_company = company_repository.get_by_id(db, recruiter.company_id)
        if not db_company:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Company not found"
            )
            
        # Verify recruiter profile doesn't already exist for this user
        db_recruiter = recruiter_repository.get_by_user_id(db, recruiter.user_id)
        if db_recruiter:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Recruiter profile already exists for this user"
            )

        return recruiter_repository.create(db, recruiter)

    def list_recruiters(self, db: Session, skip: int = 0, limit: int = 100) -> list[Recruiter]:
        return recruiter_repository.list(db, skip, limit)

    def get_recruiter(self, db: Session, recruiter_id: int) -> Recruiter:
        db_recruiter = recruiter_repository.get_by_id(db, recruiter_id)
        if not db_recruiter:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Recruiter profile not found"
            )
        return db_recruiter

recruiter_service = RecruiterService()
