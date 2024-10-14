from fastapi import HTTPException, status
from app.services.user_management_system import models
from app.shared.credentials import verify_access_token
from app.shared.dependencies import OAuth2BearerDepend, DataBaseSession


def get_current_user(
        token: OAuth2BearerDepend,
        db: DataBaseSession,
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token = verify_access_token(token, credentials_exception)

    user = db.query(models.User).filter(models.User.id == token).first()

    return user
