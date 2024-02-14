from router import tasks_router

from fastapi import  FastAPI

from contextlib import asynccontextmanager

from db import create_tables, delete_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Таблицы дропнуты")
    await create_tables()
    print("Таблицы создались")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
