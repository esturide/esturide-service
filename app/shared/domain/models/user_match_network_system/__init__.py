from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from app.shared.database import Base


class UserScore(Base):
    __tablename__ = "user_scores"

    id = Column(Integer, primary_key=True)

    passenger_id = Column(Integer, ForeignKey("passengers.id"), nullable=False)
    driver_id = Column(Integer, ForeignKey("drivers.id"), nullable=False)

    stars = Column(Integer, nullable=False)
    comment = Column(Text, nullable=False)
    review_type = Column(
        Enum("DriverToPassenger", "PassengerToDriver", name="review_type"),
        nullable=False,
    )

    driver = relationship("Driver", back_populates="user_score")
    passenger = relationship("Passenger", back_populates="user_score")


class TravelSchedule(Base):
    __tablename__ = "travel_schedule"

    id = Column(Integer, primary_key=True)

    driver_id = Column(Integer, ForeignKey("drivers.id"), nullable=False, primary_key=True)
    automobile_id = Column(Integer, ForeignKey("automobiles.id"), nullable=False)

    price = Column(Integer, nullable=False)

    initial_datetime = Column(DateTime, nullable=False)
    final_datetime = Column(DateTime, nullable=False)

    initial_location = Column(String, nullable=False)
    final_location = Column(String, nullable=False)

    driver = relationship("Driver", back_populates="travel")
    automobiles = relationship("Automobile", back_populates="travel")


class Ride:
    __tablename__ = "rides"

    id = Column(Integer, primary_key=True)

    passenger_id = Column(Integer, ForeignKey("passengers.id"), nullable=False)

    proposed_price = Column(Integer, nullable=False)

    initial_datetime = Column(DateTime, nullable=False)

    passenger = relationship("Passenger", back_populates="rides")


class Travel:
    __tablename__ = "travelrequests"

    id = Column(Integer, primary_key=True)

    passenger_id = Column(Integer, ForeignKey("passengers.id"), nullable=False)
    travels_id = Column(Integer, ForeignKey("travels.id"), nullable=False)

    initial_datetime = Column(DateTime, nullable=False)
