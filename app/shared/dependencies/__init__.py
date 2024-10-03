from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.shared.database import get_db

DataBaseSession = Annotated[Session, Depends(get_db())]
