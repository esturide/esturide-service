from datetime import date, timedelta
from typing import Optional

from pydantic import BaseModel, EmailStr, validator


class UserCreate(BaseModel):
    firstname: str
    maternal_surname: str
    paternal_surname: str
    password: str
    birth_date: date
    school_code: str
    email: EmailStr
    curp: str

    @validator("birth_date")
    def validate_birth_date(
        cls, value: date
    ):  # Corregido: añade 'date' como tipo de parámetro
        today = date.today()
        minimum_age = today - timedelta(days=365 * 18)
        if value > minimum_age:
            raise ValueError("The person must be of legal age")
        return value


class UserUpdatePut(BaseModel):
    email: EmailStr
    firstname: str
    middlename: str
    lastname: str


class UserUpdatePatch(BaseModel):
    email: Optional[EmailStr] = None
    firstname: Optional[str] = None
    middlename: Optional[str] = None
    lastname: Optional[str] = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    firstname: str
    middlename: str
    lastname: str
    curp: str
    valid_user: bool

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
