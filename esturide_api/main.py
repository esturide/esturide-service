from typing import List, Optional

from fastapi import Body, Depends, FastAPI, HTTPException, Response, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from . import models, schemas, utils
from .config.database import SessionLocal, engine, get_db
from .routers import auth, user

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
