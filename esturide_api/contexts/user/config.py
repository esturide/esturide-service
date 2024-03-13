from esturide_api.contexts.user.application.user_application import (
    UserApplicationService,
)
from esturide_api.contexts.user.domain.service.user import UserService
from esturide_api.contexts.user.infraestructure.database.user import (
    UserPostgresRepository,
)

# Aqui se arman los servicios y sus dependencias


def get_user_application_service() -> UserApplicationService:
    return UserApplicationService(get_user_service())


def get_user_service() -> UserService:
    return UserService(
        UserPostgresRepository(),
    )
