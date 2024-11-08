from typing import List, Optional

from sqlalchemy.orm import Session

from app.services.user_match_network_system.domain import models
from app.services.user_match_network_system.schemas import TravelCreate, TravelUpdate


class TravelRepository:
    @staticmethod
    def get_all(db: Session) -> List[models.Travel]:
        return db.query(models.Travel).all()

    @staticmethod
    def get_by_id(db: Session, travel_id: int) -> Optional[models.Travel]:
        return db.query(models.Travel).filter(models.Travel.id == travel_id).first()

    @staticmethod
    def create(db: Session, travel: TravelCreate) -> models.Travel:
        new_travel = models.Travel(**travel.dict())
        db.add(new_travel)
        db.commit()
        db.refresh(new_travel)
        return new_travel

    @staticmethod
    def update(
        db: Session, travel: models.Travel, travel_data: TravelCreate
    ) -> models.Travel:
        for key, value in travel_data.dict().items():
            setattr(travel, key, value)
        db.commit()
        db.refresh(travel)
        return travel

    @staticmethod
    def partial_update(
        db: Session, travel: models.Travel, travel_data: TravelUpdate
    ) -> models.Travel:
        update_data = travel_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(travel, key, value)
        db.commit()
        db.refresh(travel)
        return travel

    @staticmethod
    def delete(db: Session, travel: models.Travel) -> None:
        db.delete(travel)
        db.commit()
