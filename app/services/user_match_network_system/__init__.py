from fastapi import FastAPI

user_match_network_system_service = FastAPI(
    title="User Match Network System"
)

@user_match_network_system_service.get("/")
def index():
    return {"message": "Hello World from 'User Match Network System'"}
