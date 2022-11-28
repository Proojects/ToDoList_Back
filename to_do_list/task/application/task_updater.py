from to_do_list.task.domain.entities.task import Task
from to_do_list.task.domain.services.task_service import TaskService


class TaskUpdater:

    def __init__(self, task_service: TaskService):
        self.task_service = task_service

    def execute(self, user_id: int, task_id: Task, task: Task) -> Task:
        return self.task_service.update(user_id=user_id,
                                        task_id=task_id,
                                        task=task)
