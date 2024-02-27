from typing import Annotated
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from contextlib import asynccontextmanager
from database import create_tables, delete_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('delete')
    await create_tables()
    print('start')
    yield
    print('close')


app = FastAPI(lifespan=lifespan)

class STaskAdd(BaseModel):
    name: str
    description: str | None = None

class STask(STaskAdd):
    id: int
    

tasks = []
@app.post('/tasks')
async def add_task(task: Annotated[STaskAdd, Depends()]):
    tasks.append(task)
    return {'add': True}

# @app.get('/tasks')
# def get_home():
#     task = Task(name='bla bla')
#     return {'data': task}

