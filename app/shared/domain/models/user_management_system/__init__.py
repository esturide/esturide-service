from sqlalchemy import (
    Boolean,
    Column,
    Date,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from app.shared.database import Base


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
