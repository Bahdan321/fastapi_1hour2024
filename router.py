from typing import Annotated
from fastapi import APIRouter, Depends
from repository import TaskRepository

from schemas import STask, STaskAdd, STaskID

tasks_router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)

tasks = []

@tasks_router.post("/")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
) -> STaskID:
    task_id = await TaskRepository.add_one(task)
    return {
        "Success": True,
        "task_id": task_id,
    }

@tasks_router.get("")
async def get_all_tasks() -> list[STask]:
    tasks = await TaskRepository.get_all()
    return {
        "Success": True,
        "tasks": tasks,
    }
