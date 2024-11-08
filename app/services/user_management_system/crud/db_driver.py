from sqlalchemy.orm import Session

from app.services.user_management_system import utils, schemas
from app.shared.domain.models.user_management_system import Driver


def get_drivers_db(db: Session):
    drivers = db.query(Driver).all()
    return drivers


def get_driver_db(id: int, db: Session):
    driver = db.query(Driver).filter(Driver.id == id).first()
    utils.check_existence_by_id(
        db, Driver, id, f"Driver with id: {id} does not exist"
    )
    return driver


def create_driver_db(driver: schemas.DriverCreate, db: Session, user_id: int):
    new_driver = Driver(**driver.dict(), id=user_id)
    utils.check_not_existence_by_id(
        db, Driver, user_id, f"Driver with id: {user_id} it's already registered"
    )
    db.add(new_driver)
    db.commit()
    db.refresh(new_driver)
    return new_driver


def delete_driver_db(id: int, db: Session):
    driver = db.query(Driver).filter(Driver.id == id).first()
    utils.check_existence_by_id(
        db, Driver, id, f"Driver with id: {id} does not exist"
    )
    db.delete(driver)
    db.commit()
    return {"message": f"Driver with id {id} was successfully deleted"}


def update_driver_db(id: int, updated_driver: schemas.DriverCreate, db: Session):
    driver = db.query(Driver).filter(Driver.id == id).first()
    utils.check_existence_by_id(
        db, Driver, id, f"Driver with id: {id} does not exist"
    )
    updated_values = updated_driver.dict(exclude_unset=True)
    for key, value in updated_values.items():
        setattr(driver, key, value)
    db.commit()
    db.refresh(driver)
    return driver
