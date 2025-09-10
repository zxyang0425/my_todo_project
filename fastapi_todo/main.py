# /main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_todo.routes import tasks, auth, user
from fastapi_todo.database import create_db_and_tables
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 啟動時初始化資料庫
    create_db_and_tables()
    yield
    # 如果有需要，在這裡加上關閉資料庫或清理資源的程式

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(tasks.router)
app.include_router(user.router)