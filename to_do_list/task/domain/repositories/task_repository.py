from abc import ABC, abstractmethod
from typing import List, Optional

from ..entities.task import Task


class TaskRepository (ABC):

    @abstractmethod
    def create(self, task: Task) -> Task:
        pass
    
    @abstractmethod
    def delete(self, task_id: int) -> bool:
        pass

    @abstractmethod
    def update(self, task_id: int, task: Task) -> Task:
        pass

    @abstractmethod
    def get(self, task_id: int) -> Optional[Task]:
        pass

    @abstractmethod
    def find(self) -> Optional[List[Task]]:
        pass
