from to_do_list.task.domain.services.task_service import TaskService


class TaskFinder:

    def __init__(self, task_service: TaskService):
        self.task_service = task_service

    def execute(self):
        pass
