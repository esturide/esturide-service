from typing import List

from sqlalchemy.orm import Session

from services.user_management_system import utils, models
from services.user_management_system.contexts.user.domain.model.user_model import (
    UserCreate,
    UserUpdatePatch,
    UserUpdatePut,
)
from services.user_management_system.contexts.user.domain.repository.user_repository import UserRepository


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

    def update_user(
            self, user_id: int, updated_data: UserUpdatePut | UserUpdatePatch
    ) -> dict:
        user_query = self.db.query(models.User).filter(models.User.id == user_id)
        auxiliar_user = {k: v for k, v in updated_data.dict().items() if v is not None}
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
