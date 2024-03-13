from typing import List

from fastapi import APIRouter

from esturide_api.contexts.user.config import get_user_application_service
from esturide_api.contexts.user.domain.model.user import UserOut

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/{id}", response_model=UserOut)
def get_user(
    id: int,
):
    user_application_service = get_user_application_service()
    return user_application_service.get_user(id)


@router.get("/", response_model=List[UserOut])
def get_users():
    user_application_service = get_user_application_service()
    return user_application_service.get_users()


# Puntos de acceso de un ENDPOINT REST

# 1. Endpoint desde infraestructure/rest
# 2. (Aplicacion conecta a infraestructure y domain) -> UserApplicationService
#     Este service es el unico que tiene derecho a llamar al Servicio creado en Domain
# 3. Desde el servicio creado en Domain, se hacen llamadas a la base de datos utilizando el repository

# 4. Desde el repository se entrega resultado al servicio de Domain
# 5. El servicio de domain entrega resultado al servicio de application
# 6. El servicio de application entrega resultado al endpoint
