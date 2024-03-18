from typing import List

from fastapi import APIRouter, Depends

from esturide_api.contexts.user.application.user_service import UserApplicationService
from esturide_api.contexts.user.depencencies import get_user_application_service
from esturide_api.contexts.user.domain.model.user_model import UserOut
from esturide_api.shared.authentication.dependencies import get_request_user

router = APIRouter(prefix="/v2/users", tags=["Users"])


@router.get("/{id}", response_model=UserOut)
def get_user(
    id: int,
    user_app_service: UserApplicationService = Depends(get_user_application_service),
    current_user=Depends(get_request_user),
):
    return user_app_service.get_user(id)


@router.get("/", response_model=List[UserOut])
def get_users(
    user_app_service: UserApplicationService = Depends(get_user_application_service),
    current_user=Depends(get_request_user),
):
    return user_app_service.get_users()
