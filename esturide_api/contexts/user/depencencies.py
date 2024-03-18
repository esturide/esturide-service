from fastapi import Depends
from sqlalchemy.orm import Session

from esturide_api.config.database import get_db
from esturide_api.contexts.user.application.user_service import UserApplicationService
from esturide_api.contexts.user.domain.repository.user_repository import UserRepository
from esturide_api.contexts.user.domain.service.user_domain_service import UserService
from esturide_api.contexts.user.infraestructure.database.db_user_repository import (
    UserPostgresRepository,
)


def get_user_repository(db: Session = Depends(get_db)):
    return UserPostgresRepository(db)


def get_user_application_service(
    user_repository: UserRepository = Depends(get_user_repository),
) -> UserApplicationService:
    return UserApplicationService(UserService(user_repository))
