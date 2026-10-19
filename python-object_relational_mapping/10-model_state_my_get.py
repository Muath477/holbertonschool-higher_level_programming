#!/usr/bin/python3
"""Print the id of the State matching a name given as argument."""
import sys

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def get_state_id(username, password, database, state_name):
    """Print the id of the State called state_name, or Not found.

    The name is bound as a query parameter, so the script is safe from SQL
    injection.
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = session.query(State).filter(State.name == state_name).order_by(
        State.id).first()
    print("Not found" if state is None else state.id)
    session.close()


if __name__ == "__main__":
    get_state_id(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
