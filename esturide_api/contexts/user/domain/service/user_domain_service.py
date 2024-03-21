from typing import List

from esturide_api.contexts.user.domain.model.user_model import (
    UserCreate,
    UserOut,
    UserUpdatePatch,
    UserUpdatePut,
)
from esturide_api.contexts.user.domain.repository.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user_id: int) -> UserOut:
        return self.user_repository.get_user_by_id(user_id)

    def get_users(self) -> List[UserOut]:
        return self.user_repository.get_all_users()

    def delete_user(self, user_id: int):
        user = self.user_repository.get_user_by_id(user_id)
        if user:
            self.user_repository.delete_user(user_id)
            return {"message": f"User with id {user_id} was successfully deleted"}
        return {"message": f"User with id {user_id} was not found"}

    def update_user_put(self, user_id: int, updated_data: UserUpdatePut) -> UserOut:
        if not self.user_repository.get_user_by_id(user_id):
            return {"message": f"User with id {user_id} was not found"}
        if self.user_repository.get_user_by_email(updated_data.email):
            return {"message": "Email already registered"}
        if self.user_repository.get_user_by_curp(updated_data.curp):
            return {"message": "Curp already registered"}
        return self.user_repository.update_user_put(user_id, updated_data)

    def create_user(self, created_data: UserCreate) -> UserOut:
        if self.user_repository.get_user_by_email(created_data.email):
            return {"message": "Email already registered"}
        if self.user_repository.get_user_by_curp(created_data.curp):
            return {"message": "CURP already registered"}
        return self.user_repository.create_user(created_data)

    def update_user_patch(self, user_id: int, updated_data: UserUpdatePatch) -> UserOut:
        if not self.user_repository.get_user_by_id(user_id):
            return {"message": f"User with id {user_id} was not found"}
        if self.user_repository.get_user_by_email(updated_data.email):
            return {"message": "Email already registered"}
        if self.user_repository.get_user_by_curp(updated_data.curp):
            return {"message": "Curp already registered"}
        original_user = self.user_repository.get_user_by_id(user_id)
        return self.user_repository.update_user_patch(id, updated_data, original_user)
