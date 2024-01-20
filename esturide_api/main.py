from fastapi import FastAPI

from fastapi import Body, Depends, FastAPI, HTTPException, Response, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from esturide_api import models, schemas, utils
from esturide_api.config.database import SessionLocal, engine, get_db
from esturide_api.routers.auth import router as AuthorizationRouter
from esturide_api.routers.user import router as UserRouter

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(UserRouter)
app.include_router(AuthorizationRouter)


@app.get("/")
def read_root():
    return {"Hello": "World"}
