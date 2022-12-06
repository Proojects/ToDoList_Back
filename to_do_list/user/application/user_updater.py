from ..domain.entities.user import User
from ..domain.services.user_service import UserService


class UserUpdater:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def execute(self, user_id: int, user: User) -> User:
        return self.user_service.update(user_id=user_id, user=user)
