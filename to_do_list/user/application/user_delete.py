from ..domain.services.user_service import UserService


class UserDeleter:
    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service

    def execute(self, user_id: int) -> bool:
        return self.user_service.delete(user_id=user_id)
