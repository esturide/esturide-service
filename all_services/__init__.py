from fastapi import FastAPI

from user_management_system import user_management_system_service
from user_match_network_system import user_match_network_system_service

main = FastAPI(
    title="EstuRide API",
    servers=[
        {"url": "/", "description": "Root services"},
        {"url": "/user_management_system", "description": "User Management System"},
        {"url": "/user_match_network_system", "description": "User Match Network System"},
    ],
)

main.mount("/user_management_system", user_management_system_service)
main.mount("/user_match_network_system", user_match_network_system_service)


@main.get("/")
def index():
    return {"message": "Hello World from main service"}
