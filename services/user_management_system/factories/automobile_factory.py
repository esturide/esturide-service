from random import randint

from factory import Factory, Faker, Sequence
from sqlalchemy.orm import Session

from services.user_management_system.models import Automobile, Driver


class AutomobileFactory(Factory):
    class Meta:
        model = Automobile

    driver = Driver
    license_plates = Sequence(lambda n: f"ABCDEF{n}")
    brand = Faker(
        "random_element", elements=["Toyota", "Nissan", "Honda", "Tesla", "BMW"]
    )
    model = Faker(
        "random_element", elements=["Model1", "Model2", "Model3", "Model4", "Model5"]
    )
    year = Faker("random_int", min=2000, max=2023)
    is_insurance_active = Faker("boolean", chance_of_getting_true=50)


def create_automobiles(db: Session):
    automobile = db.query(Automobile).first()

    if automobile:
        return "Automobiles table it's already populated"

    drivers = db.query(Driver).all()

    for driver in drivers:
        num_automobiles = randint(1, 3)

        for _ in range(num_automobiles):
            automobile = AutomobileFactory.create(driver=driver)

            db.add(automobile)

    db.commit()
    return "Automobiles table it's being populated"
