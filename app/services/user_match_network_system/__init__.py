from fastapi import FastAPI

from app.services.user_match_network_system.api.routes.travels import router_travels
from app.services.user_match_network_system.api.routes.user_score import router_user_score

user_match_network_system_service = FastAPI(
    title="User Match Network System"
)

user_match_network_system_service.include_router(router_travels)
user_match_network_system_service.include_router(router_user_score)

@user_match_network_system_service.get("/")
def index():
    return {"message": "Hello World from 'User Match Network System'"}
