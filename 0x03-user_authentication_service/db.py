#!/usr/bin/env python3
"""
DataBase module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound, InvalidRequestError
from user import Base, User


class DB:
    """
    DataBase class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """add_user to add a new user in the db"""
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwarg) -> User:
        """search for an user in database"""
        for key, value in kwarg.items():
            if hasattr(User, key):
                Filter = {key: value}
                # print(Filter, *Filter)
                user = self._session.query(User).filter_by(**Filter).one()
                if user:
                    break
            else:
                raise InvalidRequestError()
        if not user:
            raise NoResultFound()
        # print(user)
        return user
