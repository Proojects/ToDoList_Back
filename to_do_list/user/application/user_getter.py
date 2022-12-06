from typing import Optional

from ..domain.entities.user import User
from ..domain.services.user_service import UserService


class UserGetter:

    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service

    def execute(self, user_id: int) -> Optional[User]:
        return self.user_service.get(user_id=user_id)
