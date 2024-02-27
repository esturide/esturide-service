from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from esturide_api import models, schemas
from esturide_api.config import database
from esturide_api.config.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

"""
There are 3 pieces of information that we need for
the token,they are:
- Secret_key
- Algorithm
- Expiration
"""
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token: OAuth2PasswordBearer, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = str(payload.get("user_id"))
        if user_id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=user_id)
    except JWTError:
        raise credentials_exception
    return token_data


def get_current_user(
    token: OAuth2PasswordBearer = Depends(oauth2_scheme),
    db: Session = Depends(database.get_db),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token = verify_access_token(token, credentials_exception)

    user = db.query(models.User).filter(models.User.id == token.id).first()

    return user
