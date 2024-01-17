from re import search
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .. import models, oauth2, schemas, utils
from ..config.database import get_db

# Prefix and tag for this router
# Prefix: localhost/users/
router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        # Hash the password
        hashed_password = utils.hash(user.password)
        user.password = hashed_password
        new_user = models.User(**user.dict())
        db.add(new_user)
        db.commit()
        return "Successful!!"
    except IntegrityError as e:
        error_str = str(e)
        # Si hay una violación de la restricción UNIQUE, lanzar una HTTPException
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


@router.get("/", response_model=List[schemas.UserOut])
def get_users(
    db: Session = Depends(get_db), current_user=Depends(oauth2.get_current_user)
):
    users = db.query(models.User).all()
    print(current_user.email)
    return users


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(
    id: int,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user),
):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id:{id} does not exist",
        )

    return user


@router.put("/{id}", response_model=schemas.UserOut)
def update_user_put(
    id: int,
    updated_user: schemas.UserUpdatePut,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user),
):
    try:
        user_query = db.query(models.User).filter(models.User.id == id)
        user = user_query.first()
        if user == None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id: {id} does not exist",
            )

        user_query.update(updated_user.dict(), synchronize_session=False)
        db.commit()
        return user_query.first()
    except IntegrityError as e:
        error_str = str(e)
        # Si hay una violación de la restricción UNIQUE, lanzar una HTTPException
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


@router.patch("/{id}", response_model=schemas.UserOut)
def update_user_patch(
    id: int,
    updated_user: schemas.UserUpdatePatch,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user),
):
    try:
        user_query = db.query(models.User).filter(models.User.id == id)
        user = user_query.first()
        if user == None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id: {id} does not exist",
            )

        user_query.update(updated_user.dict(), synchronize_session=False)
        db.commit()
        return user_query.first()
    except IntegrityError as e:
        error_str = str(e)
        # Si hay una violación de la restricción UNIQUE, lanzar una HTTPException
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


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    id: int,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user),
):

    user = db.query(models.User).filter(models.User.id == id)
    if user.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {id} does not exist",
        )

    user.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
