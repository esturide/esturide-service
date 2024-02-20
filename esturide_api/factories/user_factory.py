from bcrypt import gensalt, hashpw
from factory import Factory, Faker, Sequence
from sqlalchemy.orm import Session

from esturide_api.models import User


class UserFactory(Factory):
    class Meta:
        model = User

    firstname = Faker("first_name")
    maternal_surname = Faker("last_name")
    paternal_surname = Faker("last_name")
    password = "dummy_password"
    birth_date = Faker("date_of_birth")
    school_code = Faker("ean8")
    email = Sequence(lambda n: f"user{n}@example.com")
    curp = Sequence(lambda n: f"CURP{n}")
    valid_user = True


def create_dummy_users(db: Session, num_users: int = 100):

    user = db.query(User).first()

    if user:
        return "Users table it's already populated"

    for i in range(num_users):
        user = UserFactory.create()
        hashed_password = hashpw(user.password.encode("utf-8"), gensalt())
        user.password = hashed_password.decode("utf-8")
        if i >= 60:
            user.valid_user = False
        db.add(user)
    db.commit()
    return "Users table is being populated"
