from typing import List

from fastapi import APIRouter, Depends

from esturide_api import oauth2
from esturide_api.contexts.user.application.user_application import (
    UserApplicationService,
)
from esturide_api.contexts.user.config import get_user_application_service
from esturide_api.contexts.user.domain.model.user_model import UserOut

router = APIRouter(prefix="/v2/users", tags=["Users"])


@router.get("/{id}", response_model=UserOut)
def get_user(
    id: int,
    user_app_service: UserApplicationService = Depends(get_user_application_service),
    current_user=Depends(oauth2.get_current_user),
):
    return user_app_service.get_user(id)


@router.get("/", response_model=List[UserOut])
def get_users(
    user_app_service: UserApplicationService = Depends(get_user_application_service),
    current_user=Depends(oauth2.get_current_user),
):
    return user_app_service.get_users()
