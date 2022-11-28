from typing import List, Optional
from ..entities.task import Task


class TaskService:
    def __init__(self) -> None:
        pass

    def create(self, user_id: int, task: Task) -> Task:
        pass

    def update(self, user_id: int, task_id: Task, task: Task) -> Task:
        pass

    def delete(self, user_id: int, task_id: int) -> bool:
        pass

    def get(self, task_id: int) -> Optional[Task]:
        pass

    def find(self) -> List[Optional[Task]]:
        pass
