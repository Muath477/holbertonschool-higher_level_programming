#!/usr/bin/python3
"""Define the City class mapped to the cities table of a MySQL database."""
from relationship_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """Represent a city stored in the cities table, linked to a state."""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
