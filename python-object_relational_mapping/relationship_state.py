#!/usr/bin/python3
"""Define the State class with a relationship to its cities, and the Base."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Represent a state stored in the states table, with its cities.

    Deleting a State also deletes all the City objects linked to it, and each
    City reaches its State through the attribute named state.
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")
