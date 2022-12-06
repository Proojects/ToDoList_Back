from ..domain.services.user_service import UserService


class UserFinder:

    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def execute(self):
        pass
