from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.shared.database import Base


class UserScore(Base):
    __tablename__ = "user_scores"

    id = Column(Integer, primary_key=True, autoincrement=True)

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


class PassengerScore(Base):
    pass


class DriverScore(Base):
    pass


class TravelSchedule(Base):
    __tablename__ = "travel_schedule"

    id = Column(Integer, primary_key=True, autoincrement=True)

    driver_id = Column(Integer, ForeignKey("drivers.id"), nullable=False, primary_key=True)
    automobile_id = Column(Integer, ForeignKey("automobiles.id"), nullable=False)

    price = Column(Integer, nullable=False)

    driver = relationship("Driver", back_populates="travel")
    automobiles = relationship("Automobile", back_populates="travel")


class RideRequest(Base):
    __tablename__ = "ride_request"

    record_id = Column(Integer, ForeignKey("monitoring_record.id"), nullable=False)
    passenger_id = Column(Integer, ForeignKey("passanger.id"), nullable=False)

    passenger = relationship("Passenger", back_populates="ride_request")
    record = relationship("MonitoringRecord", back_populates="ride_request")


class TravelMatch(Base):
    __tablename__ = "travel_match"

    id = Column(Integer, primary_key=True)

    record_id = Column(Integer, ForeignKey("monitoring_record.id"), nullable=False)
    travel_id = Column(Integer, ForeignKey("travel_schedule.id"), nullable=False)
    ride_id = Column(Integer, ForeignKey("ride_request.id"), nullable=False)

    record = relationship("Passenger", back_populates="travel_match")
    travel = relationship("TravelSchedule", back_populates="travel_match")
    ride = relationship("RideRequest", back_populates="travel_match")


class TravelRoute(Base):
    __tablename__ = "travel_route"

    id = Column(Integer, primary_key=True)

    schedule_id = Column(Integer, ForeignKey("travel_schedule.id"), nullable=False)
    matching_id = Column(Integer, ForeignKey("travel_match.id"), nullable=True)
    tracking_id = Column(Integer, ForeignKey("tracking_records.id"), nullable=True)

    schedule = relationship("TravelSchedule", back_populates="travel_route")
    matching = relationship("TravelMatch", back_populates="travel_route")
    tracking = relationship("TrackingRecord", back_populates="travel_route")


class MonitoringRecord(Base):
    __tablename__ = "monitoring_records"

    id = Column(Integer, primary_key=True)

    time = Column(DateTime, nullable=False)
    ubication = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)


class TrackingRecord(Base):
    __tablename__ = "tracking_records"

    id = Column(Integer, primary_key=True)
    time = Column(DateTime, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
