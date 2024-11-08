from typing import List, Optional

from sqlalchemy.orm import Session

from app.services.user_match_network_system.domain import models
from app.services.user_match_network_system.schemas import UserScoreCreate


class UserScoreRepository:
    @staticmethod
    def get_all(db: Session) -> List[models.UserScore]:
        return db.query(models.UserScore).all()

    @staticmethod
    def get_by_id(db: Session, user_score_id: int) -> Optional[models.UserScore]:
        return (
            db.query(models.UserScore)
            .filter(models.UserScore.id == user_score_id)
            .first()
        )

    @staticmethod
    def create(db: Session, user_score: UserScoreCreate) -> models.UserScore:
        new_user_score = models.UserScore(**user_score.dict())
        db.add(new_user_score)
        db.commit()
        db.refresh(new_user_score)
        return new_user_score

    @staticmethod
    def delete(db: Session, user_score: models.UserScore) -> None:
        db.delete(user_score)
        db.commit()
