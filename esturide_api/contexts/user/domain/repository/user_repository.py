from abc import ABC, abstractmethod
from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from esturide_api.config.database import get_db


# Repositorio de dominio especifica las operaciones que la BD debe realizar
# No nos importa la base de datos sino, unicamente sus operaciones
class UserRepository(ABC):
    @abstractmethod
    def get_user_by_id(self, id: int, db: Session = Depends(get_db)) -> dict:
        pass

    @abstractmethod
    def get_all_users(self, db: Session = Depends(get_db)) -> List[dict]:
        pass
