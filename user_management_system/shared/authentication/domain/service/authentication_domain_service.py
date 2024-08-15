from datetime import datetime, timedelta

from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from user_management_system.config.config import settings
from user_management_system.contexts.user.domain.model.user_model import UserOut
from user_management_system.contexts.user.domain.repository.user_repository import UserRepository
from user_management_system.shared.authentication.infraestructure.oauth import PasswordHandler

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


class AuthenticationService:
    def __init__(
        self, user_repository: UserRepository, password_handler: PasswordHandler
    ):
        self.user_repository = user_repository
        self.password_handler = password_handler

    def authenticate_user(self, user_credentials) -> int:
        user = self.user_repository.get_user_by_email(user_credentials.username)

        if not user or not self.password_handler.verify(
            user_credentials.password, user.password
        ):
            self.raise_invalid_credentials_error()

        return user.id

    def generate_token(self, user_id: int) -> dict:
        expire_time = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode = {"user_id": user_id, "exp": expire_time}
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": encoded_jwt}

    def verify_access_token(self, token: OAuth2PasswordBearer) -> UserOut:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id = str(payload.get("user_id"))
            if user_id is None:
                raise self.raise_invalid_token_error()
        except JWTError:
            raise self.raise_invalid_token_error()
        return UserOut.from_orm(self.user_repository.get_user_by_id(user_id))

    def raise_invalid_credentials_error(self):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials"
        )

    def raise_invalid_token_error(self):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid JWT Token"
        )
