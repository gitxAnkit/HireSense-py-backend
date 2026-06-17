from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository:
    def get_by_id(self, db: Session, user_id: int) -> User:
        return db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, db: Session, email: str) -> User:
        return db.query(User).filter(User.email == email).first()

    def list(self, db: Session, skip: int = 0, limit: int = 100) -> list[User]:
        return db.query(User).offset(skip).limit(limit).all()

    def create(self, db: Session, name: str, email: str, phone: str, role: str, password_hash: str) -> User:
        db_user = User(
            name=name,
            email=email,
            phone=phone,
            role=role,
            password_hash=password_hash
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

user_repository = UserRepository()
