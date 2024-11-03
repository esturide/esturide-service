from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.services.user_match_network_system.domain import models
from app.services.user_match_network_system.schemas import (
    UserScoreCreate,
    UserScoreRead,
)
from app.shared.database import get_db

router = APIRouter(prefix="/user_score", tags=["user_score"])

# Rutas para UserScores
@router.get("/", response_model=List[UserScoreRead])
def get_user_scores(
    db: Session = Depends(get_db),
):
    user_scores = db.query(models.UserScore).all()
    return user_scores


@router.post("/", response_model=UserScoreRead)
def create_user_score(
    user_score: UserScoreCreate,
    db: Session = Depends(get_db),
):
    new_user_score = models.UserScore(**user_score.dict())
    db.add(new_user_score)
    db.commit()
    db.refresh(new_user_score)
    return new_user_score


@router.get("/{user_score_id}", response_model=UserScoreRead)
def get_user_score_by_id(
    user_score_id: int,
    db: Session = Depends(get_db),
):
    user_score = (
        db.query(models.UserScore).filter(models.UserScore.id == user_score_id).first()
    )
    if not user_score:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"UserScore with id: {user_score_id} was not found",
        )
    return user_score


@router.delete("/{user_score_id}", status_code=status.HTTP_200_OK)
def delete_user_score(
    user_score_id: int,
    db: Session = Depends(get_db),
):
    user_score = (
        db.query(models.UserScore).filter(models.UserScore.id == user_score_id).first()
    )
    if not user_score:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"UserScore with id: {user_score_id} was not found",
        )
    db.delete(user_score)
    db.commit()
    return {"message": f"UserScore with id: {user_score_id} was successfully deleted"}
