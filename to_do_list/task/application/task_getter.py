from typing import Optional

from ..domain.entities.task import Task
from ..domain.services.task_service import TaskService


class TaskGetter:

    def __init__(self, task_service: TaskService):
        self.task_service = task_service

    def execute(self, task_id: int) -> Optional[Task]:
        return self.task_service.get(task_id=task_id)
