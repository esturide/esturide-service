from datetime import datetime

from pydantic import BaseModel


class UserScoreCreate(BaseModel):
    passenger_id: int
    driver_id: int
    stars: int
    comment: str
    review_type: str


class UserScoreRead(UserScoreCreate):
    id: int


class TravelCreate(BaseModel):
    passenger_id: int
    driver_id: int
    automobile_id: int
    price: float
    initial_datetime: datetime
    final_datetime: datetime
    initial_location: str
    final_location: str


class TravelRead(TravelCreate):
    id: int
