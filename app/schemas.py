from pydantic import BaseModel

class JobBase(BaseModel):
    title: str
    company: str
    skills: str
    location: str
    salary: str

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int

    class Config:
        from_attributes = True
