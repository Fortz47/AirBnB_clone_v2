#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete')

    else:
        name = ""

        @property
        def cities(self):
            """Returns the list of `City` class instances attribute
            """
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
