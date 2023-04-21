#!/usr/bin/python3
"""This modules defines a City class """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """
    A city class, inherits from Base.

    Args:
        Base: class factory that generates a base class for declarative models.

    Attributes:
    __tablename__:tablename
    id:a column of integer
    name:a column of a string
    state_id: column of an integer
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
