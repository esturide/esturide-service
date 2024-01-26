from re import search

from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from esturide_api import models, schemas, utils


def get_users_db(db: Session):
    users = db.query(models.User).all()
    return users


def get_user_db(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {id} does not exist",
        )

    return user


def create_user_db(user: schemas.UserCreate, db: Session):
    try:
        hashed_password = utils.hash(user.password)
        user.password = hashed_password
        new_user = models.User(**user.dict())
        db.add(new_user)
        db.commit()
        return new_user

    except IntegrityError as e:
        error_str = str(e)
        if search("UNIQUE constraint failed: users.email", error_str):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )
        elif search("UNIQUE constraint failed: users.curp", error_str):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="CURP already registered",
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal Server Error",
            )


def delete_user_db(db: Session, id: int):
    user = db.query(models.User).filter(models.User.id == id)
    if user.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {id} does not exist",
        )

    user.delete(synchronize_session=False)
    db.commit()
    return {"message": f"User with id {id} was successfully deleted"}


def put_user_db(id: int, updated_user: schemas.UserUpdatePut, db: Session):
    try:
        user_query = db.query(models.User).filter(models.User.id == id)
        user = user_query.first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id: {id} does not exist",
            )
        auxiliar_user = updated_user.dict()
        user_query.update(auxiliar_user, synchronize_session=False)
        db.commit()
        return user_query.first()
    except IntegrityError as e:
        error_str = str(e)
        if search("UNIQUE constraint failed: users.email", error_str):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )
        elif search("UNIQUE constraint failed: users.curp", error_str):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="CURP already registered",
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal Server Error",
            )


def patch_user_db(id: int, updated_user: schemas.UserUpdatePut, db: Session):
    try:
        user_query = db.query(models.User).filter(models.User.id == id)
        user = user_query.first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id: {id} does not exist",
            )

        for field in updated_user.dict().keys():
            if hasattr(models.User, field) and getattr(updated_user, field) is not None:
                setattr(user, field, getattr(updated_user, field))

        db.commit()
        db.refresh(user)
        return user_query.first()
    except IntegrityError as e:
        error_str = str(e)
        if search("UNIQUE constraint failed: users.email", error_str):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )
        elif search("UNIQUE constraint failed: users.curp", error_str):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="CURP already registered",
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal Server Error",
            )
