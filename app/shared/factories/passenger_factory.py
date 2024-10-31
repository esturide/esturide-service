from factory import Factory
from sqlalchemy.orm import Session

from app.shared.domain.models.user_management_system import Passenger, User


class PassengerFactory(Factory):
    class Meta:
        model = Passenger

    user = User


def create_passengers_for_valid_user(db: Session):
    valid_users = db.query(User).filter(User.valid_user == True).all()
    passenger = db.query(Passenger).first()

    if passenger:
        return "Passengers table it's already populated."

    for user in valid_users:
        passenger = PassengerFactory.create(user=user)

        db.add(passenger)

    db.commit()
    return "Passengers table it's being populated"
