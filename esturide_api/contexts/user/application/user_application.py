from typing import List

from esturide_api.contexts.user.domain.model.user_model import UserOut
from esturide_api.contexts.user.domain.service.user_domain_service import UserService


class UserApplicationService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def get_user(
        self,
        user_id: int,
    ) -> UserOut:
        user = self.user_service.get_user(user_id)
        return user

    def get_users(self) -> List[UserOut]:
        return self.user_service.get_users()
