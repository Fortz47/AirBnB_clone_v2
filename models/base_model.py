#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), nullable=False, primary_key=True, unique=True)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k in ('created_at', 'updated_at'):
                        v = datetime.fromisoformat(v)
                    setattr(self, k, v)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        dict_obj = self.__dict__.copy()
        dict_obj.pop('_sa_instance_state', None)
        return '[{}] ({}) {}'.format(cls, self.id, dict_obj)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.pop('_sa_instance_state', None)
        # dictionary.update({'__class__':
        #                  (str(type(self)).split('.')[-1]).split('\'')[0]})
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            dictionary['created_at'] = self.created_at.isoformat()
            dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """deletes current instance"""
        storage.delete(self)
