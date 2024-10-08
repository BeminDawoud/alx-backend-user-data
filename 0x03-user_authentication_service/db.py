#!/usr/bin/env python3
"""DB module
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class"""

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Adds a new user"""
        try:
            new_user = User(email=email, hashed_password=hashed_password)
            self._session.add(new_user)
            self._session.commit()
        except Exception:
            self._session.rollback()
            new_user = None
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Searches for a user in the DB"""
        query = self._session.query(User)
        try:
            for key, value in kwargs.items():
                column = getattr(User, key, None)
                if column:
                    query = query.filter(column == value)
                else:
                    raise InvalidRequestError
            result = query.one()
            return result
        except (InvalidRequestError, NoResultFound):
            raise

    def update_user(self, user_id: int, **kwargs) -> None:
        """Updates a user in the DB"""
        try:
            query = self._session.query(User)
            user = query.filter(User.id == user_id).one()
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
                else:
                    raise ValueError
            self._session.add(user)
            self._session.commit()
        except Exception as e:
            self._session.rollback()
            raise e
