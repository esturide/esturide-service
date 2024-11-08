from factory import Factory
from sqlalchemy.orm import Session

from app.shared.domain.models.user_management_system import Driver, User


class DriverFactory(Factory):
    class Meta:
        model = Driver

    user = None
    is_driver_license_active = True


def create_dummy_drivers(db: Session, num_drivers: int = 25):
    driver = db.query(Driver).first()
    if driver:
        return "Drivers table it's already populated."

    valid_users = db.query(User).filter(User.valid_user == True).all()

    num_created = 0

    for user in valid_users:
        if num_created >= num_drivers:
            break
        driver = DriverFactory.create(user=user)
        db.add(driver)

        num_created += 1

    db.commit()
    return "Drivers table is being populated"
