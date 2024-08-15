from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from user_management_system.config.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    firstname = Column(String, nullable=False)
    maternal_surname = Column(String, nullable=False)
    paternal_surname = Column(String, nullable=False)
    password = Column(String, nullable=False)
    birth_date = Column(Date)
    school_code = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    curp = Column(String, nullable=False, unique=True)
    valid_user = Column(Boolean, server_default="FALSE", nullable=False)

    driver = relationship("Driver", uselist=False, back_populates="user")
    passenger = relationship("Passenger", uselist=False, back_populates="user")


class Driver(Base):
    __tablename__ = "drivers"
    id = Column(Integer, ForeignKey("users.id"), primary_key=True, nullable=False)
    is_driver_license_active = Column(Boolean, server_default="FALSE", nullable=False)

    user = relationship("User", back_populates="driver")
    automobiles = relationship("Automobile", back_populates="driver")
    user_score = relationship("UserScore", back_populates="driver")
    travel = relationship("Travel", uselist=False, back_populates="driver")


class Automobile(Base):
    __tablename__ = "automobiles"

    id = Column(Integer, primary_key=True)
    driver_id = Column(Integer, ForeignKey("drivers.id"), nullable=False)
    license_plates = Column(String, nullable=False, unique=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    is_insurance_active = Column(Boolean, nullable=False, default=False)

    # Define la relación con el conductor
    driver = relationship("Driver", back_populates="automobiles")
    travel = relationship("Travel", uselist=False, back_populates="automobiles")


class Passenger(Base):
    __tablename__ = "passengers"
    id = Column(Integer, ForeignKey("users.id"), primary_key=True, nullable=False)

    user = relationship("User", back_populates="passenger")
    user_score = relationship("UserScore", back_populates="passenger")
    travel = relationship("Travel", uselist=False, back_populates="passenger")


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


class Travel(Base):
    __tablename__ = "travels"
    id = Column(Integer, primary_key=True)
    passenger_id = Column(Integer, ForeignKey("passengers.id"), nullable=False)
    driver_id = Column(
        Integer, ForeignKey("drivers.id"), nullable=False, primary_key=True
    )
    automobile_id = Column(Integer, ForeignKey("automobiles.id"), nullable=False)
    price = Column(Float, nullable=False)
    initial_datetime = Column(DateTime, nullable=False)
    final_datetime = Column(DateTime, nullable=False)
    initial_location = Column(String, nullable=False)
    final_location = Column(String, nullable=False)

    driver = relationship("Driver", back_populates="travel")
    passenger = relationship("Passenger", back_populates="travel")
    automobiles = relationship("Automobile", back_populates="travel")
