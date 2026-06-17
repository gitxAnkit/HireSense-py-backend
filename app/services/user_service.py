from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.core.security import hash_password
from app.repositories.user_repository import user_repository
from app.schemas.user import UserCreate
from app.models.user import User

class UserService:
    def create_user(self, db: Session, user: UserCreate) -> User:
        db_user = user_repository.get_by_email(db, user.email)
        if db_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        password_hash = hash_password(user.password)
        return user_repository.create(
            db=db,
            name=user.name,
            email=user.email,
            phone=user.phone,
            role=user.role,
            password_hash=password_hash
        )

    def list_users(self, db: Session, skip: int = 0, limit: int = 100) -> list[User]:
        return user_repository.list(db, skip, limit)

    def get_user(self, db: Session, user_id: int) -> User:
        db_user = user_repository.get_by_id(db, user_id)
        if not db_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return db_user

user_service = UserService()
