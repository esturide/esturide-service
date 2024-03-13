# Se recomienda tener un metodo dentro del Service por cada endpoint

from typing import List

from esturide_api.contexts.user.domain.model.user import UserOut
from esturide_api.contexts.user.domain.repository.user import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user_id: int) -> UserOut:
        # Cada vez que quiera hacer una interaccion a base de datos, tengo que llamar al repositorio
        return self.user_repository.get_user_by_id(user_id)

    def get_users(self) -> List[UserOut]:
        return self.user_repository.get_all_users()
