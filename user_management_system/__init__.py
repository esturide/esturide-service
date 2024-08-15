from fastapi import FastAPI, HTTPException

from user_management_system import models
from user_management_system.config.database import engine
from user_management_system.contexts.user.domain.errors import UserServiceValidationError
from user_management_system.contexts.user.infraestructure.router.user_router import (
    router as V2_UserRouter,
)
from user_management_system.routers.auth import router as AuthorizationRouter
from user_management_system.routers.automobile import router as AutomobileRouter
from user_management_system.routers.drivers import router as DriverRouter
from user_management_system.routers.populate_db import router as DBRouter
from user_management_system.routers.user import router as UserRouter
from user_management_system.shared.authentication.infraestructure.router.authentication_router import (
    router as V2_AuthorizationRouter,
)

models.Base.metadata.create_all(bind=engine)
user_management_system_service = FastAPI(
    title="User Management System"
)

user_management_system_service.include_router(UserRouter)
user_management_system_service.include_router(AuthorizationRouter)
user_management_system_service.include_router(DriverRouter)
user_management_system_service.include_router(AutomobileRouter)
user_management_system_service.include_router(DBRouter)
user_management_system_service.include_router(V2_UserRouter)
user_management_system_service.include_router(V2_AuthorizationRouter)


@user_management_system_service.exception_handler(UserServiceValidationError)
def user_service_validation_exception_handler(request, exc: UserServiceValidationError):
    raise HTTPException(status_code=400, detail=str(exc))
