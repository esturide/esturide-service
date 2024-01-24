from sqlalchemy import Boolean, Column, Integer, String

from esturide_api.config.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    firstname = Column(String, nullable=False)
    middlename = Column(String, nullable=True)
    lastname = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    curp = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    valid_user = Column(Boolean, server_default="FALSE", nullable=False)
