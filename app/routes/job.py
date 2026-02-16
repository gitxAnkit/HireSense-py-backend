from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from database import SessionLocal, engine




router = APIRouter(
    prefix="/job",
    tags=["Job"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Job)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
    db_job = models.Job(**job.model_dump())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

@router.get("/", response_model=list[schemas.Job])
def get_jobs(db: Session = Depends(get_db)):
    jobs = db.query(models.Job).all()
    return jobs
