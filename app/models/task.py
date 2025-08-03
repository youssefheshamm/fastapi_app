from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from app.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)


class TaskCreate(BaseModel):
    title: str
    description: str
