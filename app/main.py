from fastapi import FastAPI
from app.routes import job
from app import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="HireSense API")

app.include_router(job.router)

@app.get("/")
def root():
    return {"message": "HireSense Backend Running"}
