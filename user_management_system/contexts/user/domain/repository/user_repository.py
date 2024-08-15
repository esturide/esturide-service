from abc import ABC, abstractmethod
from typing import List

from user_management_system.contexts.user.domain.model.user_model import (
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
    def update_user(
            self, id: int, updated_data: UserUpdatePut | UserUpdatePatch
    ) -> dict:
        pass

    @abstractmethod
    def create_user(self, created_data: UserCreate) -> dict:
        pass
