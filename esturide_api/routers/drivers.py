from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from esturide_api import oauth2, schemas
from esturide_api.config.database import get_db
from esturide_api.crud import db_driver as driver_functions

router = APIRouter(prefix="/drivers", tags=["Drivers"])


@router.get("/", response_model=List[schemas.DriverResponse])
def get_drivers(
    db: Session = Depends(get_db), current_user=Depends(oauth2.get_current_user)
):
    return driver_functions.get_drivers_db(db)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.DriverResponse
)
def create_driver(
    driver: schemas.DriverCreate,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user),
):
    return driver_functions.create_driver_db(driver, db, current_user.id)


@router.get("/{id}", response_model=schemas.DriverResponse)
def get_driver(
    id: int,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user),
):
    return driver_functions.get_driver_db(id, db)


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_driver(
    id: int,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user),
):
    return driver_functions.delete_driver_db(id, db)


@router.put("/{id}", response_model=schemas.DriverResponse)
def update_driver(
    id: int,
    updated_driver: schemas.DriverCreate,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user),
):
    return driver_functions.update_driver_db(id, updated_driver, db)
