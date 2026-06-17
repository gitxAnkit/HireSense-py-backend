from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.user import User, UserCreate
from app.services.user_service import user_service

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.
    Hashes the password using SHA-256 for basic security without external dependencies.
    """
    return user_service.create_user(db, user)

@router.get("/", response_model=List[User])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve all users.
    Supports pagination via `skip` and `limit`.
    """
    return user_service.list_users(db, skip, limit)

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single user by ID.
    Raises a 404 error if user does not exist.
    """
    return user_service.get_user(db, user_id)
