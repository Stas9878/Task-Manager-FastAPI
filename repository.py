from sqlalchemy import select
from database import new_session, TaskOrm
from schemas import STaskAdd, STask

class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()
            task = TaskOrm(**task_dict)

            session.add(task)
            await session.flush()
            await session.commit()
            return int(task.id)

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [task for task in task_models]
            return task_schemas