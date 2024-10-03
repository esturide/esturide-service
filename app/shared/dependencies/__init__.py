from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core import oauth2_scheme
from app.shared.database import get_db

OAuth2BearerDepend = Annotated[OAuth2PasswordBearer, Depends(oauth2_scheme)]
DataBaseSession = Annotated[Session, Depends(get_db)]
