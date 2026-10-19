#!/usr/bin/python3
"""Print the first State object of a MySQL database using SQLAlchemy."""
import sys

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def print_first_state(username, password, database):
    """Print the State with the lowest id, or Nothing if the table is empty."""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    print_first_state(sys.argv[1], sys.argv[2], sys.argv[3])
