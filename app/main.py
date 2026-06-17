from fastapi import FastAPI
from app.routes import job, user, company, recruiter
from app import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="HireSense API")

app.include_router(user.router)
app.include_router(company.router)
app.include_router(recruiter.router)
app.include_router(job.router)
 
 
@app.get("/")
def root():
    return {"message": "HireSense Backend Running"}
