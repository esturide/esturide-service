from datetime import date, timedelta

from fastapi import HTTPException, status
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from services.user_management_system import models

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def validate_age(birth_date: date):
    today = date.today()
    minimum_age = today - timedelta(days=365 * 16)
    if birth_date > minimum_age:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User must be at least 16 years old",
        )


def check_existence_by_criteria(
        db: Session, model_name: str, criteria: dict, error_message: str
):
    model = getattr(models, model_name)
    existing_record = db.query(model).filter_by(**criteria).first()
    if existing_record:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error_message,
        )


def check_existence_by_id(db: Session, model: type, id: int, error_message: str):
    existing_record = db.query(model).filter_by(id=id).first()
    if not existing_record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error_message,
        )


def check_not_existence_by_id(db: Session, model: type, id: int, error_message: str):
    existing_record = db.query(model).filter_by(id=id).first()
    if existing_record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error_message,
        )
