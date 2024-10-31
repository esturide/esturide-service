from fastapi import APIRouter
from fastapi import FastAPI

from app.services.user_management_system import user_management_system_service
from app.shared.domain.models.user_management_system import Automobile, Driver, Passenger, User
from app.services.user_match_network_system import user_match_network_system_service
from app.shared.domain.models.user_match_network_system import UserScore, Travel
from app.shared.dependencies import DataBaseSession
from app.shared.factories.automobile_factory import create_automobiles
from app.shared.factories.driver_factory import create_dummy_drivers
from app.shared.factories.passenger_factory import create_passengers_for_valid_user
from app.shared.factories.travel_factory import create_multiple_travels
from app.shared.factories.user_factory import create_dummy_users
from app.shared.factories.user_score_factory import generate_user_scores

populate_router = APIRouter(tags=["Factories"])

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


@root.post("/populate")
def populate_db(db: DataBaseSession):
    print(create_dummy_users(db))
    print(create_passengers_for_valid_user(db))
    print(create_dummy_drivers(db))
    print(create_automobiles(db))
    print(create_multiple_travels(db))
    print(generate_user_scores(db))

    return {
        "message": "DB populated"
    }


@root.delete("/clear")
def clear_db(db: DataBaseSession):
    db.query(UserScore).delete()
    db.query(Travel).delete()
    db.query(Automobile).delete()
    db.query(Driver).delete()
    db.query(Passenger).delete()
    db.query(User).delete()
    db.commit()

    return {
        "message": "DB cleared"
    }
