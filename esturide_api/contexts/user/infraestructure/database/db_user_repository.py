from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from esturide_api import models
from esturide_api.config.database import get_db
from esturide_api.contexts.user.domain.repository.user import UserRepository


class UserPostgresRepository(UserRepository):
    def get_user_by_id(self, id: int, db: Session = Depends(get_db)) -> dict:
        return db.query(models.User).filter(models.User.id == id).first()

    def get_all_users(self, db: Session = Depends(get_db)) -> List[dict]:
        return db.query(models.User).all()
