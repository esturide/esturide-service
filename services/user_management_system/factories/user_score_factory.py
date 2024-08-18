from random import randint

from factory import Factory, Faker, Sequence
from sqlalchemy.orm import Session

from services.user_management_system.models import Travel, UserScore


class UserScoreFactory(Factory):
    class Meta:
        model = UserScore

    passenger_id = None
    driver_id = None
    stars = Faker("random_int", min=1, max=5)
    comment = Faker("text")
    review_type = Sequence(
        lambda n: "DriverToPassenger" if n % 2 == 0 else "PassengerToDriver"
    )


def generate_user_scores(db: Session):
    user_score = db.query(UserScore).first()

    if user_score:
        return "User scores table it's already populated."

    travels = db.query(Travel).all()

    for travel in travels:
        existing_score = (
            db.query(UserScore)
            .filter_by(passenger_id=travel.passenger_id, driver_id=travel.driver_id)
            .first()
        )
        if not existing_score:
            driver_to_passenger_review = UserScore(
                passenger_id=travel.passenger_id,
                driver_id=travel.driver_id,
                stars=randint(1, 5),
                comment="Driver to Passenger review",
                review_type="DriverToPassenger",
            )
            db.add(driver_to_passenger_review)

            passenger_to_driver_review = UserScore(
                passenger_id=travel.passenger_id,
                driver_id=travel.driver_id,
                stars=randint(1, 5),
                comment="Passenger to Driver review",
                review_type="PassengerToDriver",
            )
            db.add(passenger_to_driver_review)
    db.commit()
    return "User scores it's being populated"
