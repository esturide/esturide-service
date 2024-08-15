from fastapi import FastAPI

from user_management_system import user_management_system_service

main = FastAPI(
    title="EstuRide API"
)

main.mount("/user_management_system", user_management_system_service)


@main.get("/")
def read_root():
    return {"message": "Hello World from main service"}
