from abc import ABC, abstractmethod
from typing import List

from esturide_api.contexts.user.domain.model.user_model import (
    UserBase,
    UserCreate,
    UserUpdatePatch,
    UserUpdatePut,
)


class UserRepository(ABC):
    @abstractmethod
    def get_user_by_id(self, id: int) -> dict:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> dict:
        pass

    @abstractmethod
    def get_user_by_curp(self, curp: str) -> dict:
        pass

    @abstractmethod
    def get_all_users(self) -> List[dict]:
        pass

    @abstractmethod
    def delete_user(self, id: int):
        pass

    @abstractmethod
    def update_user_put(self, id: int, updated_data: UserUpdatePut) -> dict:
        pass

    @abstractmethod
    def create_user(self, created_data: UserCreate) -> dict:
        pass

    @abstractmethod
    def update_user_patch(
        self, id: int, created_data: UserUpdatePatch, original_data: UserBase
    ) -> dict:
        pass
