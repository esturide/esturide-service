from sqlalchemy.orm import Session

from esturide_api.config.database import SessionLocal
from esturide_api.factories.passenger_factory import create_passengers_for_valid_user
from esturide_api.factories.user_factory import create_dummy_users

Session = SessionLocal()
create_dummy_users(Session)
create_passengers_for_valid_user(Session)
Session.close()
