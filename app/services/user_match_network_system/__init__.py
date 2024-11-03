from fastapi import FastAPI

from app.services.user_match_network_system.routers.travel import (
    router as travel_router,
)
from app.services.user_match_network_system.routers.userScore import (
    router as user_score_router,
)

user_match_network_system_service = FastAPI(title="User Match Network System")

user_match_network_system_service.include_router(user_score_router)
user_match_network_system_service.include_router(travel_router)


@user_match_network_system_service.get("/")
def index():
    return {"message": "Hello World from 'User Match Network System'"}
