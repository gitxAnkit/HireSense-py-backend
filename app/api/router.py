from fastapi import APIRouter
from app.api.endpoints import users, jobs, companies, recruiters

api_router = APIRouter()

api_router.include_router(users.router)
api_router.include_router(companies.router)
api_router.include_router(recruiters.router)
api_router.include_router(jobs.router)
