from typing import Optional
from app import utils
from app.db import models
from app.db.сonnection import get_db
from sqlalchemy.orm import Session


class AuthProvider:
    def __init__(self):
        pass

    def register(self, email: str, password: str) -> Optional[str]:
        if self._user_exists(email):
            return 'user already exists'
        self._register_user(email, password)

    def authenticate(self, email: str, password: str) -> Optional[str]:
        if not self._password_match(email, password):
            return 'email or password is incorrect'

    def _user_exists(self, email: str) -> bool:
        return False

    def _register_user(self, email: str, password: str):
        pass

    def _password_match(self, email: str, password: str) -> bool:
        return False


class TempAuthProvider(AuthProvider):
    def __init__(self):
        super().__init__()
        self.users: dict[str, str] = dict()

    def _user_exists(self, email: str) -> bool:
        return email in self.users

    def _register_user(self, email: str, password: str):
        print(utils.hash_password(password))
        self.users[email] = utils.hash_password(password)

    def _password_match(self, email: str, password: str) -> bool:
        return self._user_exists(email) and \
            utils.verify_password(password, self.users[email])


class PostgresAuthProvider(AuthProvider):
    def __init__(self, db: Session = next(get_db())):
        super().__init__()
        self.database = db

    def _user_exists(self, email: str) -> bool:
        user: models.User = self.database\
            .query(models.User)\
            .filter(models.User.email == email)\
            .one_or_none()
        return user is not None

    def _register_user(self, email: str, password: str):
        new_user = models.User(email=email, password=utils.hash_password(password))
        self.database.add(new_user)
        self.database.commit()
        self.database.refresh(new_user)

    def _password_match(self, email: str, password: str) -> bool:
        user: models.User = self.database\
            .query(models.User)\
            .filter(models.User.email == email)\
            .one_or_none()
        return user is not None and \
            utils.verify_password(password, user.password)


provider = PostgresAuthProvider()
