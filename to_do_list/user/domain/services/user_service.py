from typing import List, Optional
from ..entities.user import User


class UserService:
    def __init__(self) -> None:
        pass

    def create(self, user_id: int, user: User) -> User:
        pass

    def update(self, user_id: int, user: User) -> User:
        pass

    def delete(self, user_id: int) -> bool:
        pass

    def get(self, user_id: int) -> Optional[User]:
        pass

    def find(self) -> List[Optional[User]]:
        pass
