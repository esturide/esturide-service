from passlib.context import CryptContext


class PasswordHandler:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash(self, password: str):
        return self.pwd_context.hash(password)

    def verify(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)
