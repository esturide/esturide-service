from typing import List

from sqlalchemy.orm import Session

from esturide_api import models
from esturide_api.contexts.user.domain.repository.user_repository import UserRepository


class UserPostgresRepository(UserRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_id(self, id: int) -> dict:
        return self.db.query(models.User).filter(models.User.id == id).first()

    def get_user_by_email(self, email: str) -> dict:
        return self.db.query(models.User).filter(models.User.email == email).first()

    def get_all_users(self) -> List[dict]:
        return self.db.query(models.User).all()

    def delete_user(self, id: int) -> dict:
        user = self.db.query(models.User).filter(models.User.id == id)
        user.delete(synchronize_session=False)
        self.db.commit()
        return {"message": f"User with id {id} was successfully deleted"}
