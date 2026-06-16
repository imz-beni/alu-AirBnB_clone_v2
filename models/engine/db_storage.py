#!/usr/bin/python3
"""This module defines a class to manage DB storage for hbnb clone"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
            'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
          }


class DBStorage:
    """This class manages storage of hbnb models using SQLAlchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate the DBStorage engine"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db),
            pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects, optionally filtered by class"""
        result = {}
        if cls is not None:
            if isinstance(cls, str):
                cls = classes.get(cls)
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                result[key] = obj
        else:
            for c in classes.values():
                objs = self.__session.query(c).all()
                for obj in objs:
                    key = '{}.{}'.format(type(obj).__name__, obj.id)
                    result[key] = obj
        return result

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and the current database session"""
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(factory)

    def close(self):
        """Close the current session"""
        self.__session.remove()
