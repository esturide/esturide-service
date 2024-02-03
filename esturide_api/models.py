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

from esturide_api.config.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    firstname = Column(String(64), nullable=False)
    maternal_surname = Column(String(64), nullable=False)
    paternal_surname = Column(String(64), nullable=False)
    password = Column(String(32), nullable=False)
    birth_date = Column(Date)
    school_code = Column(String(32), nullable=False)
    email = Column(String(64), nullable=False)
    curp = Column(String(64), nullable=False)
    valid_user = Column(Boolean, server_default="FALSE", nullable=False)

    # Si queremos que sea relacion uno a uno debemos setear uselist a False
    passenger = relationship("Passenger", uselist=False, back_populates="user")
    driver = relationship("Driver", uselist=False, back_populates="user")


class Passenger(Base):
    __tablename__ = "passengers"
    id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )

    # Definimos la relacion inversa con la tabla user (es decir si desde esta tabla podemos acceder
    # A los datos del usuario)
    user = relationship("User", back_populates="passenger")
    user_scores = relationship("UserScore", back_populates="passenger")
    travel = relationship("Travel", back_populates="passenger")


class Driver(Base):
    __tablename__ = "drivers"
    id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )
    is_driver_license_active = Column(Boolean, server_default="FALSE", nullable=False)

    user = relationship("User", back_populates="driver")
    automobiles = relationship("Automobile", back_populates="driver")
    user_scores = relationship("UserScore", back_populates="driver")
    travel = relationship("Travel", back_populates="driver")


class Automobile(Base):
    __tablename__ = "automobiles"
    id = Column(Integer, primary_key=True, nullable=False)
    driver_id = Column(
        Integer, ForeignKey("drivers.id", ondelete="CASCADE"), nullable=False
    )
    license_plates = Column(String(32), nullable=False)
    brand = Column(String(32), nullable=False)
    model = Column(String(32), nullable=False)
    year = Column(Integer, nullable=False)
    is_insurance_active = Column(Boolean, server_default="FALSE", nullable=False)

    driver = relationship("Driver", back_populates="automobiles")
    travel = relationship("Travel", back_populates="automobiles")


class UserScore(Base):
    __tablename__ = "user_scores"
    passenger_id = Column(
        Integer, ForeignKey("passengers.id"), primary_key=True, nullable=False
    )
    driver_id = Column(
        Integer, ForeignKey("drivers.id"), primary_key=True, nullable=False
    )
    stars = Column(Integer, nullable=False)
    comment = Column(Text, nullable=False)
    review_type = Column(
        Enum("DriverToPassenger", "PassengerToDriver", name="review_types"),
        nullable=False,
    )

    passenger = relationship("Passenger", back_populates="user_scores")
    driver = relationship("Driver", back_populates="user_scores")


class Travel(Base):
    __tablename__ = "travels"
    id = Column(Integer, primary_key=True, nullable=False)
    passenger_id = Column(Integer, ForeignKey("passengers.id"), nullable=False)
    driver_id = Column(Integer, ForeignKey("drivers.id"), nullable=False)
    automobile_id = Column(Integer, ForeignKey("automobiles.id"), nullable=False)
    price = Column(Float, nullable=False)
    initial_datetime = Column(DateTime, nullable=False)
    final_datetime = Column(DateTime, nullable=False)
    initial_location = Column(String(255), nullable=False)
    final_location = Column(String(255), nullable=False)

    passenger = relationship("Passenger", uselist=False, back_populates="travel")
    driver = relationship("Driver", uselist=False, back_populates="travel")
    automobile = relationship("Automobile", uselist=False, back_populates="travel")
