from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.services.user_management_system import oauth2, schemas
from app.services.user_management_system.config.database import get_db
from app.services.user_management_system.crud import db_user as user_functions

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return user_functions.create_user_db(user, db)


@router.get("/", response_model=List[schemas.UserOut])
def get_users(
        db: Session = Depends(get_db), current_user=Depends(oauth2.get_current_user)
):
    return user_functions.get_users_db(db)


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(
        id: int,
        db: Session = Depends(get_db),
        current_user=Depends(oauth2.get_current_user),
):
    return user_functions.get_user_db(id, db)


@router.put("/{id}", response_model=schemas.UserOut)
def update_user_put(
        id: int,
        updated_user: schemas.UserUpdatePut,
        db: Session = Depends(get_db),
        current_user=Depends(oauth2.get_current_user),
):
    return user_functions.put_user_db(id, updated_user, db)


@router.patch("/{id}", response_model=schemas.UserOut)
def update_user_patch(
        id: int,
        updated_user: schemas.UserUpdatePatch,
        db: Session = Depends(get_db),
        current_user=Depends(oauth2.get_current_user),
):
    return user_functions.patch_user_db(id, updated_user, db)


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_user(
        id: int,
        db: Session = Depends(get_db),
        current_user=Depends(oauth2.get_current_user),
):
    return user_functions.delete_user_db(db, id)
