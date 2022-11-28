from ..domain.entities.task import Task
from ..domain.services.task_service import TaskService


class TaskCreator:
    def __init__(self, task_service: TaskService):
        self.task_service = task_service

    def execute(self, user_id: int, task: Task) -> Task:
        return self.task_service.create(user_id=user_id,
                                        task=task)
