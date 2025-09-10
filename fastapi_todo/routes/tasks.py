from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from typing import List

from fastapi_todo.models.task import Task
from fastapi_todo.dependencies import get_current_user
from fastapi_todo.models.user import User
from fastapi_todo.schemas.task import TaskCreate, TaskRead, TaskUpdate
from fastapi_todo.database import get_session

router = APIRouter()

@router.get("/tasks", response_model=List[TaskRead])
def get_tasks(session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    tasks = session.exec(select(Task).where(Task.user_id == current_user.id)).all()
    return tasks

@router.post("/tasks", response_model=TaskRead)
def create_task(task_data: TaskCreate, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    task = Task.from_orm(task_data)
    task.user_id = current_user.id
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@router.get("/tasks/{task_id}", response_model=TaskRead)
def get_task(task_id: int, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    task = session.get(Task, task_id)
    if not task or task.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}", response_model=TaskRead)
def update_task(task_id: int, task_data: TaskUpdate, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    task = session.get(Task, task_id)
    if not task or task.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Task not found")

    task_data_dict = task_data.model_dump(exclude_unset=True)
    for key, value in task_data_dict.items():
        setattr(task, key, value)

    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    task = session.get(Task, task_id)
    if not task or task.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Task not found")
    session.delete(task)
    session.commit()
    return {"detail": "Task deleted"}