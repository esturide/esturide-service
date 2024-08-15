from fastapi import APIRouter, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from user_management_system.shared.authentication.application.authentication_service import (
    AuthenticationApplicationService,
)
from user_management_system.shared.authentication.dependencies import (
    get_authentication_application_service,
)
from user_management_system.shared.authentication.domain.model.authentication_model import Token

router = APIRouter(prefix="/v2", tags=["Authentication"])


@router.post("/login", response_model=Token)
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    authentication_app_service: AuthenticationApplicationService = Depends(
        get_authentication_application_service
    ),
):
    return authentication_app_service.authenticate_user(user_credentials)
