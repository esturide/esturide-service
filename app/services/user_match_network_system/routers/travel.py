from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.services.user_match_network_system.domain import models
from app.services.user_match_network_system.schemas import (
    TravelCreate,
    TravelRead,
    TravelUpdate,
)
from app.shared.database import get_db

router = APIRouter(prefix="/travel", tags=["travel"])


@router.get("/", response_model=List[TravelRead])
def get_travels(
    db: Session = Depends(get_db),
):
    travels = db.query(models.Travel).all()
    return travels


@router.get("/{travel_id}", response_model=TravelRead)
def get_travel_by_id(
    travel_id: int,
    db: Session = Depends(get_db),
):
    travel = db.query(models.Travel).filter(models.Travel.id == travel_id).first()
    if not travel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Travel with id: {travel_id} was not found",
        )
    return travel


@router.post("/", response_model=TravelRead)
def create_travel(
    travel: TravelCreate,
    db: Session = Depends(get_db),
):
    new_travel = models.Travel(**travel.dict())
    db.add(new_travel)
    db.commit()
    db.refresh(new_travel)
    return new_travel


@router.put("/{travel_id}", response_model=TravelRead)
def update_travel(
    travel_id: int,
    travel_update: TravelCreate,
    db: Session = Depends(get_db),
):
    travel = db.query(models.Travel).filter(models.Travel.id == travel_id).first()
    if not travel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Travel with id: {travel_id} was not found",
        )

    # Reemplazar todos los campos con los datos proporcionados
    for key, value in travel_update.dict().items():
        setattr(travel, key, value)

    db.commit()
    db.refresh(travel)
    return travel


@router.patch("/{travel_id}", response_model=TravelRead)
def partial_update_travel(
    travel_id: int,
    travel_update: TravelUpdate,
    db: Session = Depends(get_db),
):
    travel = db.query(models.Travel).filter(models.Travel.id == travel_id).first()
    if not travel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Travel with id: {travel_id} was not found",
        )

    update_data = travel_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(travel, key, value)

    db.commit()
    db.refresh(travel)
    return travel


@router.delete("/{travel_id}", status_code=status.HTTP_200_OK)
def delete_travel(
    travel_id: int,
    db: Session = Depends(get_db),
):
    travel = db.query(models.Travel).filter(models.Travel.id == travel_id).first()
    if not travel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Travel with id: {travel_id} was not found",
        )
    db.delete(travel)
    db.commit()
    return {"message": f"Travel with id: {travel_id} was successfully deleted"}
