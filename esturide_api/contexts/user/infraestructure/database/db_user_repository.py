from typing import List

from sqlalchemy.orm import Session

from esturide_api import models, utils
from esturide_api.contexts.user.domain.model.user_model import (
    UserBase,
    UserCreate,
    UserUpdatePatch,
    UserUpdatePut,
)
from esturide_api.contexts.user.domain.repository.user_repository import UserRepository


class UserPostgresRepository(UserRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_id(self, id: int) -> dict:
        return self.db.query(models.User).filter(models.User.id == id).first()

    def get_user_by_email(self, email: str) -> dict:
        return self.db.query(models.User).filter(models.User.email == email).first()

    def get_user_by_curp(self, curp: str) -> dict:
        return self.db.query(models.User).filter(models.User.curp == curp).first()

    def get_all_users(self) -> List[dict]:
        return self.db.query(models.User).all()

    def delete_user(self, id: int):
        user = self.db.query(models.User).filter(models.User.id == id)
        user.delete(synchronize_session=False)
        self.db.commit()

    def update_user_put(self, user_id: int, updated_data: UserUpdatePut) -> dict:
        user_query = self.db.query(models.User).filter(models.User.id == user_id)
        auxiliar_user = updated_data.dict()
        user_query.update(auxiliar_user, synchronize_session=False)
        self.db.commit()
        return user_query.first()

    def create_user(self, created_data: UserCreate) -> dict:
        hashed_password = utils.hash(created_data.password)
        created_data.password = hashed_password
        new_user = models.User(**created_data.dict())
        self.db.add(new_user)
        self.db.commit()
        return new_user

    def update_user_patch(
        self, id: int, updated_data: UserUpdatePatch, original_data: UserBase
    ) -> dict:
        for field in updated_data.dict().keys():
            if hasattr(models.User, field) and getattr(updated_data, field) is not None:
                setattr(original_data, field, getattr(updated_data, field))

        self.db.commit()
        self.db.refresh(original_data)
        return self.get_user_by_id(id)
