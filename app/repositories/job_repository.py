from sqlalchemy.orm import Session
from app.models.job import Job
from app.schemas.job import JobCreate

class JobRepository:
    def get_by_id(self, db: Session, job_id: int) -> Job:
        return db.query(Job).filter(Job.id == job_id).first()

    def list(self, db: Session, skip: int = 0, limit: int = 100) -> list[Job]:
        return db.query(Job).order_by(Job.updated_at.desc(), Job.created_at.desc()).offset(skip).limit(limit).all()

    def create(self, db: Session, job: JobCreate) -> Job:
        db_job = Job(**job.model_dump())
        db.add(db_job)
        db.commit()
        db.refresh(db_job)
        return db_job

job_repository = JobRepository()
