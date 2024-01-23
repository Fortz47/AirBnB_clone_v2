#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import relationship

lk_table = Table("place_amenity", Base.metadata,
                 Column("place_id", String(60), ForeignKey("places.id"),
                        primary_key=True, nullable=False),
                 Column("amenity_id", String(60), ForeignKey("amenities.id"),
                        primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))  # nullable=True
        number_rooms = Column(Integer, default=0)  # nullable=False
        number_bathrooms = Column(Integer, default=0)  # nullable=False
        max_guest = Column(Integer, default=0)  # nullable=False
        price_by_night = Column(Integer, default=0)  # nullable=False
        latitude = Column(Float)  # nullable=True
        longitude = Column(Float)  # nullable=True
        reviews = relationship("Review", cascade="all, delete", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ Get a list of all linked reviews. """
            reviewList = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    reviewList.append(review)
            return reviewList

        @property
        def amenities(self):
            """Gets linked Amenities"""
            amenityList = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenityList

        @amenities.setter
        def amenities(self, value):
            """Adds an Amenity.id to the attribute amenity_ids"""
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
