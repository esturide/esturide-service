from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.services.user_management_system import oauth2, schemas
from app.shared.database import get_db
from app.shared.domain.models.user_management_system import Automobile, Driver

router = APIRouter(prefix="/automobiles", tags=["Automobiles"])


@router.get("/", response_model=List[schemas.AutomobileResponse])
def get_automobiles(
        db: Session = Depends(get_db), current_user=Depends(oauth2.get_current_user)
):
    drivers = db.query(Automobile).all()
    return drivers


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.AutomobileResponse
)
def create_automobile(
        automobile: schemas.AutomobileCreate,
        db: Session = Depends(get_db),
        current_user=Depends(oauth2.get_current_user),
):
    driver = db.query(Driver).filter(Driver.id == current_user.id).first()

    if not driver:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="You are not yet a driver"
        )

    new_automobile = Automobile(**automobile.dict(), driver_id=current_user.id)

    db.add(new_automobile)
    db.commit()
    db.refresh(new_automobile)

    return new_automobile


@router.get("/{id}", response_model=schemas.AutomobileResponse)
def get_automobile_by_id(
        id: int,
        db: Session = Depends(get_db),
        current_user=Depends(oauth2.get_current_user),
):
    automobile = db.query(Automobile).filter(Automobile.id == id).first()
    if not automobile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Automobile with id: {id} was not found",
        )
    return automobile


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_automobile(
        id: int,
        db: Session = Depends(get_db),
        current_user=Depends(oauth2.get_current_user),
):
    automobile = db.query(Automobile).filter(Automobile.id == id).first()
    if not automobile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Automobile with id: {id} was not found",
        )
    db.delete(automobile)
    db.commit()
    return {"message": f"Automobile with id: {id} was successfully deleted"}
