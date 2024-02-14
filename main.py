from typing import Annotated, Optional

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from contextlib import asynccontextmanager

from db import create_tables, delete_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Таблицы дропнуты")
    await create_tables()
    print("Таблицы создались")
    yield
    print("База готова")

app = FastAPI()

tasks = []

class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

class Stask(STaskAdd):
    id: int

@app.post("/tasks")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
):
    tasks.append(task)
    return {
        "Success": True,
        "task": task,
    }

# @app.post("/tasks")
# async def get_tasks(name: str, desc: str = None):
#     task = Task(name=name,description=desc)
#     tasks.append(task)
#     return {
#         "Success": True,
#         "data": task,
#     }

# @app.get("/tasks")
# async def get_all_tasks():
#     return {
#         "data": tasks,
#     }