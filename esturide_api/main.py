from fastapi import FastAPI
from .config.database import SessionLocal,engine,get_db
from typing import Optional,List
from fastapi import Body, FastAPI,Response,status,HTTPException,Depends
from pydantic import BaseModel
from . import models,schemas,utils
from sqlalchemy.orm import Session
from .routers import user,auth

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
