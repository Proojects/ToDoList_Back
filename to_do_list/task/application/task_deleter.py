from ..domain.services.task_service import TaskService


class TaskDeleter:

    def __init__(self, task_service: TaskService):
        self.task_service = task_service

    def execute(self, user_id: int, task_id: int) -> bool:
        return self.task_service.delete(user_id=user_id,
                                        task_id=task_id)
