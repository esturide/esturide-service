from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from esturide_api.config.database import get_db
from esturide_api.factories.automobile_factory import create_automobiles
from esturide_api.factories.driver_factory import create_dummy_drivers
from esturide_api.factories.passenger_factory import create_passengers_for_valid_user
from esturide_api.factories.travel_factory import create_multiple_travels
from esturide_api.factories.user_factory import create_dummy_users
from esturide_api.factories.user_score_factory import generate_user_scores
from esturide_api.models import Automobile, Driver, Passenger, Travel, User, UserScore

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
