from typing import Optional
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email:EmailStr
    firstname: str
    middlename: str
    lastname: str
    curp: str
    password:str

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class UserOut(BaseModel):
    id:int
    email:EmailStr
    firstname: str
    middlename: str
    lastname: str
    curp: str
    valid_user:bool

    class Config:
        from_attributes=True

class Token(BaseModel):
    access_token:str
    token_type: str

class TokenData(BaseModel):
    id:Optional[str]=None