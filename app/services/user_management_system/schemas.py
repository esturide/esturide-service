from datetime import date, timedelta
from typing import Optional

from pydantic import BaseModel, EmailStr, validator


class UserBase(BaseModel):
    firstname: str
    maternal_surname: str
    paternal_surname: str
    password: str
    birth_date: date
    school_code: str
    email: EmailStr
    curp: str


class UserCreate(UserBase):
    @validator("birth_date")
    def validate_birth_date(cls, value: date):
        today = date.today()
        minimum_age = today - timedelta(days=365 * 16)
        if value > minimum_age:
            raise ValueError("The person must be of legal age")
        return value


class UserUpdatePut(BaseModel):
    email: EmailStr
    firstname: str
    maternal_surname: str
    paternal_surname: str
    curp: str
    birth_date: date


class UserUpdatePatch(BaseModel):
    email: Optional[EmailStr] = None
    firstname: Optional[str] = None
    maternal_surname: Optional[str] = None
    paternal_surname: Optional[str] = None
    curp: Optional[str] = None
    birth_date: Optional[date] = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    firstname: str
    maternal_surname: str
    paternal_surname: str
    curp: str
    valid_user: bool

    class Config:
        from_attributes = True


class DriverCreate(BaseModel):
    is_driver_license_active: bool


class DriverResponse(BaseModel):
    is_driver_license_active: bool

    user: UserOut


class AutomobileBase(BaseModel):
    license_plates: str
    brand: str
    model: str
    year: int
    is_insurance_active: bool


class AutomobileCreate(AutomobileBase):
    pass


class AutomobileResponse(AutomobileBase):
    id: int
    driver_id: int
    driver: DriverResponse


class AutomobilePut(BaseModel):
    pass


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
