from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from user_management_system.config.database import get_db
from user_management_system.factories.automobile_factory import create_automobiles
from user_management_system.factories.driver_factory import create_dummy_drivers
from user_management_system.factories.passenger_factory import create_passengers_for_valid_user
from user_management_system.factories.travel_factory import create_multiple_travels
from user_management_system.factories.user_factory import create_dummy_users
from user_management_system.factories.user_score_factory import generate_user_scores
from user_management_system.models import Automobile, Driver, Passenger, Travel, User, UserScore

router = APIRouter(tags=["Populate"])


@router.post("/populateDB")
def populateDB(db: Session = Depends(get_db)):

    print(create_dummy_users(db))
    print(create_passengers_for_valid_user(db))
    print(create_dummy_drivers(db))
    print(create_automobiles(db))
    print(create_multiple_travels(db))
    print(generate_user_scores(db))
    return {"message": "DB populated"}


@router.delete("/clearDB")
def clearDB(db: Session = Depends(get_db)):
    db.query(UserScore).delete()
    db.query(Travel).delete()
    db.query(Automobile).delete()
    db.query(Driver).delete()
    db.query(Passenger).delete()
    db.query(User).delete()
    db.commit()
    return {"message": "DB cleared"}
