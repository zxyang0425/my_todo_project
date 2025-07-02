from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware

#建立 FastAPI App
app = FastAPI()


#CORS設定，讓前端可以存取
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # 或是設定成你的前端網址 http://localhost:8080
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# 資料模型定義
# -------------------------------

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    done: bool = False

# -------------------------------
# 資料庫初始化
# -------------------------------

sqlite_url = "sqlite:///./task.db"
engine = create_engine(sqlite_url, echo=True)

#建立資料表
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

# -------------------------------
# CRUD 路由
# -------------------------------

#讀取所有任務
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    with Session(engine) as session:
        tasks = session.exec(select(Task)).all()
        return tasks

#新增任務
@app.post("/task", response_model=Task)
def create_task(task: Task):
    with Session(engine) as session:
        session.add(task)
        session.commit()
        session.refresh(task)  # 取得自動產生的 id
        return task


#查詢單一任務
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    with Session(engine) as session:
        task = session.get(Task, task_id) #(你要查的資料表, 這筆資料的id是多少)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task

#更新任務
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, update_task: Task):
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        task.title = update_task.title
        task.description = update_task.description
        task.done = update_task.done
        session.commit()
        session.refresh(task)
        return task
    
#刪除任務
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if not task:
            raise HTTPException(statue_code=404, detail="Task not found")
        session.delete(task)
        session.commit()
        return {"detail": "Task deleted"}


