from fastapi import FastAPI

from app.services.user_management_system import user_management_system_service
from app.services.user_match_network_system import user_match_network_system_service

root = FastAPI(
    title="EstuRide Service API",
    servers=[
        {"url": "/", "description": "Root app"},
        {"url": "/user_management_system", "description": "User Management System"},
        {"url": "/user_match_network_system", "description": "User Match Network System"},
    ],
)

root.mount("/user_management_system", user_management_system_service)
root.mount("/user_match_network_system", user_match_network_system_service)


@root.get("/")
def index():
    return {"message": "Hello World from main service"}
