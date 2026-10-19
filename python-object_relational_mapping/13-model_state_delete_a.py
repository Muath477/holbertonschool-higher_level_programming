#!/usr/bin/python3
"""Delete the State objects containing the letter a from a MySQL database."""
import sys

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def delete_states_with_a(username, password, database):
    """Delete every State whose name contains an a and save the change."""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    for state in session.query(State).filter(State.name.like("%a%")).all():
        session.delete(state)
    session.commit()
    session.close()


if __name__ == "__main__":
    delete_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])
