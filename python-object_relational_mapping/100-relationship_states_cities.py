#!/usr/bin/python3
"""Create the State California with the City San Francisco in a database."""
import sys

from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def create_state_with_city(username, password, database):
    """Create the tables, then save California with its city San Francisco.

    The city is added through the cities relationship of the State, so it is
    saved together with its state.
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = State(name="California")
    state.cities.append(City(name="San Francisco"))
    session.add(state)
    session.commit()
    session.close()


if __name__ == "__main__":
    create_state_with_city(sys.argv[1], sys.argv[2], sys.argv[3])
