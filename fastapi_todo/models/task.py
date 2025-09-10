# /models/task.py
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from fastapi_todo.models.user import User

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    done: bool = False
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")

    user: Optional[User] = Relationship(back_populates="tasks")
