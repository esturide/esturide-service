from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.services.user_management_system import utils, models, schemas


def get_users_db(db: Session):
    users = db.query(models.User).all()
    return users


def get_user_db(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    utils.check_existence_by_id(
        db, models.User, id, f"User with id: {id} does not exist"
    )
    return user


def create_user_db(user: schemas.UserCreate, db: Session):
    utils.check_existence_by_criteria(
        db, "User", {"email": user.email}, "Email already registered"
    )
    utils.check_existence_by_criteria(
        db, "User", {"curp": user.curp}, "CURP already registered"
    )
    try:
        hashed_password = utils.hash(user.password)
        user.password = hashed_password
        new_user = models.User(**user.dict())
        db.add(new_user)
        db.commit()
        return new_user

    except IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )


def delete_user_db(db: Session, id: int):
    user = db.query(models.User).filter(models.User.id == id)
    utils.check_existence_by_id(
        db, models.User, id, f"User with id: {id} does not exist"
    )

    user.delete(synchronize_session=False)
    db.commit()
    return {"message": f"User with id {id} was successfully deleted"}


def put_user_db(id: int, updated_user: schemas.UserUpdatePut, db: Session):
    utils.check_existence_by_id(
        db, models.User, id, f"User with id: {id} does not exist"
    )
    utils.check_existence_by_criteria(
        db, "User", {"email": updated_user.email}, "Email already registered"
    )
    utils.check_existence_by_criteria(
        db, "User", {"curp": updated_user.curp}, "CURP already registered"
    )
    utils.validate_age(updated_user.birth_date)
    try:
        user_query = db.query(models.User).filter(models.User.id == id)
        auxiliar_user = updated_user.dict()
        user_query.update(auxiliar_user, synchronize_session=False)
        db.commit()
        return user_query.first()

    except IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )


def patch_user_db(id: int, updated_user: schemas.UserUpdatePatch, db: Session):
    try:
        user_query = db.query(models.User).filter(models.User.id == id)
        user = user_query.first()
        utils.check_existence_by_id(
            db, models.User, id, f"User with id: {id} does not exist"
        )

        if updated_user.email:
            utils.check_existence_by_criteria(
                db, "User", {"email": updated_user.email}, "Email already registered"
            )

        if updated_user.curp:
            utils.check_existence_by_criteria(
                db, "User", {"curp": updated_user.curp}, "CURP already registered"
            )
        if updated_user.birth_date:
            utils.validate_age(updated_user.birth_date)

        for field in updated_user.dict().keys():
            if hasattr(models.User, field) and getattr(updated_user, field) is not None:
                setattr(user, field, getattr(updated_user, field))

        db.commit()
        db.refresh(user)
        return user_query.first()

    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )
