#!/usr/bin/env python3
"""authentication module"""
from db import DB
from bcrypt import hashpw, gensalt, checkpw
from user import User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """methods that hashed password"""
    return hashpw(password.encode(), gensalt())


def _generate_uuid() -> str:
    """generate uuid based on uuid module"""
    from uuid import uuid4
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register user based on email and password"""
        try:
            self._db.find_user_by(email=email)
        except (InvalidRequestError, NoResultFound):
            return self._db.add_user(email, _hash_password(password))
        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """Check Valid login"""
        try:
            user = self._db.find_user_by(email=email)
            if checkpw(password.encode(), user.hashed_password):
                return True
        except (InvalidRequestError, NoResultFound):
            return False
        return False

    def create_session(self, email: str) -> str:
        """Create session id using uuid"""
        try:
            user = self._db.find_user_by(email=email)
        except (InvalidRequestError, NoResultFound):
            return None
        user.session_id = _generate_uuid()
        return user.session_id
