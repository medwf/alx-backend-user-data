#!/usr/bin/env python3
"""authentication module"""
from db import DB
from bcrypt import hashpw, gensalt
from user import User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """methods that hashed password"""
    return hashpw(password.encode(), gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register user based on email and password"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {user.email} already exists")
        except (InvalidRequestError, NoResultFound):
            hashPassword = _hash_password(password)
            user = self._db.add_user(email, hashPassword)
            return user
