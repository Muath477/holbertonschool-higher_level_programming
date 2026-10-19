#!/usr/bin/python3
"""List the State objects containing the letter a, using SQLAlchemy."""
import sys

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def list_states_with_a(username, password, database):
    """Print each State whose name contains an a as "id: name", by id."""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    states = session.query(State).filter(State.name.like("%a%")).order_by(
        State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    list_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])
