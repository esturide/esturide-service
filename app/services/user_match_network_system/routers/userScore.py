from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.services.user_match_network_system.domain.repositorys.user_score_repository import (
    UserScoreRepository,
)
from app.services.user_match_network_system.schemas import (
    UserScoreCreate,
    UserScoreRead,
)
from app.shared.database import get_db

router = APIRouter(prefix="/user_score", tags=["user_score"])


@router.get("/", response_model=List[UserScoreRead])
def get_user_scores(db: Session = Depends(get_db)):
    return UserScoreRepository.get_all(db)


@router.get("/{user_score_id}", response_model=UserScoreRead)
def get_user_score_by_id(user_score_id: int, db: Session = Depends(get_db)):
    user_score = UserScoreRepository.get_by_id(db, user_score_id)
    if not user_score:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"UserScore with id: {user_score_id} was not found",
        )
    return user_score


@router.post("/", response_model=UserScoreRead)
def create_user_score(user_score: UserScoreCreate, db: Session = Depends(get_db)):
    return UserScoreRepository.create(db, user_score)


@router.delete("/{user_score_id}", status_code=status.HTTP_200_OK)
def delete_user_score(user_score_id: int, db: Session = Depends(get_db)):
    user_score = UserScoreRepository.get_by_id(db, user_score_id)
    if not user_score:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"UserScore with id: {user_score_id} was not found",
        )
    UserScoreRepository.delete(db, user_score)
    return {"message": f"UserScore with id: {user_score_id} was successfully deleted"}
