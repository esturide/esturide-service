from fastapi import FastAPI

from esturide_api import models
from esturide_api.config.database import engine
from esturide_api.routers.auth import router as AuthorizationRouter
from esturide_api.routers.user import router as UserRouter

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(UserRouter)
app.include_router(AuthorizationRouter)


@app.get("/")
def read_root():
    return {"Hello": "World"}
