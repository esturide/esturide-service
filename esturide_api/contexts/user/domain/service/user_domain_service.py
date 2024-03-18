from typing import List

from esturide_api.contexts.user.domain.model.user_model import UserOut, UserUpdatePut
from esturide_api.contexts.user.domain.repository.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user_id: int) -> UserOut:
        return self.user_repository.get_user_by_id(user_id)

    def get_users(self) -> List[UserOut]:
        return self.user_repository.get_all_users()

    def delete_user(self, user_id: int):
        if self.user_repository.get_user_by_id(user_id):
            self.user_repository.delete_user(user_id)
            return {"message": f"User with id {user_id} was successfully deleted"}
        return {"message": f"User with id {user_id} was not found"}

    def update_user_put(self, user_id: int, updated_data: UserUpdatePut):
        pass
