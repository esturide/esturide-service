from random import choice

from factory import Factory, Faker, Sequence
from sqlalchemy.orm import Session

from user_management_system.models import Automobile, Driver, Passenger, Travel


class TravelFactory(Factory):
    class Meta:
        model = Travel

    id = Sequence(lambda n: n)
    driver_id = None
    passenger_id = None
    automobile_id = None
    price = Faker("pyfloat", left_digits=3, right_digits=2, positive=True)
    initial_datetime = Faker("date_time_between", start_date="-1y", end_date="now")
    final_datetime = Faker("date_time_between", start_date="now", end_date="+1y")
    initial_location = Faker("address")
    final_location = Faker("address")


def create_single_travel(db: Session):
    driver = choice(
        db.query(Driver).filter(Driver.is_driver_license_active == True).all()
    )
    passenger = choice(db.query(Passenger).filter(Passenger.id != driver.id).all())
    automobile = choice(
        db.query(Automobile).filter(Automobile.driver_id == driver.id).all()
    )

    data = {
        "driver_id": driver.id,
        "passenger_id": passenger.id,
        "automobile_id": automobile.id,
    }
    travel = TravelFactory(**data)
    db.add(travel)
    db.commit()


def create_multiple_travels(db: Session, num_travels: int = 150):
    travel = db.query(Travel).first()
    if travel:
        return "Travels table it's already populated"
    for _ in range(num_travels):
        create_single_travel(db)

    return "Travels table is being populated"
