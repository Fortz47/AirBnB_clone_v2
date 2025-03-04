#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from os import getenv


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        text = ""
        place_id = ""
        user_id = ""
