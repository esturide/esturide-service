from typing import List

from fastapi import HTTPException

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

    def create_user(self, created_data: UserCreate) -> UserOut:
        validations = [
            (self._validate_unique_email, (created_data.email,)),
            (self._validate_unique_curp, (created_data.curp,)),
        ]
        validation_error = self._execute_validations(validations)
        if validation_error:
            return validation_error

        return self.user_repository.create_user(created_data)

    def update_user_put(self, user_id: int, updated_data: UserUpdatePut) -> UserOut:
        validations = [
            (self._validate_user_exists, (user_id,)),
            (self._validate_unique_email, (updated_data.email,)),
            (self._validate_unique_curp, (updated_data.curp,)),
        ]
        validation_error = self._execute_validations(validations)
        if validation_error:
            return validation_error

        return self.user_repository.update_user(user_id, updated_data)

    def update_user_patch(self, user_id: int, updated_data: UserUpdatePatch) -> UserOut:
        validations = [
            (self._validate_user_exists, (user_id,)),
            (self._validate_unique_email, (updated_data.email,)),
            (self._validate_unique_curp, (updated_data.curp,)),
        ]
        validation_error = self._execute_validations(validations)
        if validation_error:
            return validation_error

        return self.user_repository.update_user(user_id, updated_data)

    def delete_user(self, user_id: int):
        validations = [
            (self._validate_user_exists, (user_id,)),
        ]
        validation_error = self._execute_validations(validations)
        if validation_error:
            return validation_error

        self.user_repository.delete_user(user_id)
        return {"message": f"User with id {user_id} was successfully deleted"}

    def _execute_validations(self, validations):
        for validate, args in validations:
            # Proceed only if there's at least one non-None value in args
            if any(arg is not None for arg in args):
                try:
                    validate(*args)
                except ValueError as e:
                    raise HTTPException(status_code=400, detail=f"{str(e)}")

    def _validate_user_exists(self, user_id: int):
        if not self.user_repository.get_user_by_id(user_id):
            raise ValueError(f"User with id {user_id} was not found")

    def _validate_unique_email(self, email: str):
        if self.user_repository.get_user_by_email(email):
            raise ValueError("Email already registered")

    def _validate_unique_curp(self, curp: str):
        if self.user_repository.get_user_by_curp(curp):
            raise ValueError("CURP already registered")
