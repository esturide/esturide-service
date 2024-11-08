from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.services.user_match_network_system.domain.repositorys.travel_repository import (
    TravelRepository,
)
from app.services.user_match_network_system.schemas import (
    TravelCreate,
    TravelRead,
    TravelUpdate,
)
from app.shared.database import get_db

router = APIRouter(prefix="/travel", tags=["travel"])


@router.get("/", response_model=List[TravelRead])
def get_travels(db: Session = Depends(get_db)):
    return TravelRepository.get_all(db)


@router.get("/{travel_id}", response_model=TravelRead)
def get_travel_by_id(travel_id: int, db: Session = Depends(get_db)):
    travel = TravelRepository.get_by_id(db, travel_id)
    if not travel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Travel with id: {travel_id} was not found",
        )
    return travel


@router.post("/", response_model=TravelRead)
def create_travel(travel: TravelCreate, db: Session = Depends(get_db)):
    return TravelRepository.create(db, travel)


@router.put("/{travel_id}", response_model=TravelRead)
def update_travel(
    travel_id: int, travel_update: TravelCreate, db: Session = Depends(get_db)
):
    travel = TravelRepository.get_by_id(db, travel_id)
    if not travel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Travel with id: {travel_id} was not found",
        )
    return TravelRepository.update(db, travel, travel_update)


@router.patch("/{travel_id}", response_model=TravelRead)
def partial_update_travel(
    travel_id: int, travel_update: TravelUpdate, db: Session = Depends(get_db)
):
    travel = TravelRepository.get_by_id(db, travel_id)
    if not travel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Travel with id: {travel_id} was not found",
        )
    return TravelRepository.partial_update(db, travel, travel_update)


@router.delete("/{travel_id}", status_code=status.HTTP_200_OK)
def delete_travel(travel_id: int, db: Session = Depends(get_db)):
    travel = TravelRepository.get_by_id(db, travel_id)
    if not travel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Travel with id: {travel_id} was not found",
        )
    TravelRepository.delete(db, travel)
    return {"message": f"Travel with id: {travel_id} was successfully deleted"}
