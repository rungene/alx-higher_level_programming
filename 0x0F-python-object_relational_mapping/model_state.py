#!/usr/bin/python3
"""This modules defnes a State class """
from sqlalchemy import Column, Integer, String, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    A State class, inherits from Base.

    Args:
        Base: class factory that generates a base class for declarative models.

    Attributes:
    __tablename__ : MySQL table
    id:a column of integer
    name:a column of a string
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
