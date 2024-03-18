from esturide_api.contexts.user.domain.model.user_model import UserOut
from esturide_api.shared.authentication.domain.service.authentication_domain_service import (
    AuthenticationService,
)


class AuthenticationApplicationService:
    def __init__(self, auth_service: AuthenticationService):
        self.auth_service = auth_service

    def authenticate_user(self, user_credentials) -> dict:
        user_id = self.auth_service.authenticate_user(user_credentials)
        return self.auth_service.generate_token(user_id)

    def get_request_user(self, token: str) -> UserOut:
        return self.auth_service.verify_access_token(token)
