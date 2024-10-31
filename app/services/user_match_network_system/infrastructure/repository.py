from typing import Tuple

from sqlalchemy.orm import Session

from app.shared.domain.models.user_match_network_system import Travel, UserScore


class UserScoreRepository:
    def __init__(self, db: Session):
        self.db = db

    async def create(
            self, passenger_id: int, driver_id: int, stars: int, comment: str
    ) -> Tuple[bool, UserScore]:

        user_score = UserScore(
            passenger_id=passenger_id,
            driver_id=driver_id,
            stars=stars,
            comment=comment,
        )

        self.db.add(user_score)
        self.db.commit()

        return True, user_score


class TravelRepository:
    def __init__(self, db: Session):
        self.db = db

    async def create(
        self, passenger_id: int, driver_id: int, automobile_id: int, price: float
    ) -> Tuple[bool, Travel]:
        travel = Travel(
            passenger_id=passenger_id,
            driver_id=driver_id,
            automobile_id=automobile_id,
            price=price,
        )

        self.db.add(travel)
        self.db.commit()

        return True, travel
