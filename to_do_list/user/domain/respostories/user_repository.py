from abc import ABC, abstractmethod
from typing import List, Optional

from ..entities.user import User


class UserRepository (ABC):

    @abstractmethod
    def create(self, user: User) -> User:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def update(self, user_id: int, user: User) -> User:
        pass

    @abstractmethod
    def get(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    def find(self) -> Optional[List[User]]:
        pass
