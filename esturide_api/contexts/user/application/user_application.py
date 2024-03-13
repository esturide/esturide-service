from typing import List

from fastapi import Depends

from esturide_api import oauth2
from esturide_api.contexts.user.domain.model.user import UserOut
from esturide_api.contexts.user.domain.service.user import UserService


class UserApplicationService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def get_user(
        self, user_id: int, current_user=Depends(oauth2.get_current_user)
    ) -> UserOut:
        return self.user_service.get_user(user_id)

    def get_users(self, current_user=Depends(oauth2.get_current_user)) -> List[UserOut]:
        return self.user_service.get_users()
