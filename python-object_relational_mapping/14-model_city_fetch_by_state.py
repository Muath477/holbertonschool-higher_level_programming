#!/usr/bin/python3
"""List all the City objects of a MySQL database with their State."""
import sys

from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def list_cities(username, password, database):
    """Print each city as "state name: (city id) city name", sorted by id."""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    rows = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all()
    for state, city in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()


if __name__ == "__main__":
    list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
