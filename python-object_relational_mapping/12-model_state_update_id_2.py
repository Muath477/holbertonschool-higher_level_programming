#!/usr/bin/python3
"""Change the name of the State with id 2 in a MySQL database."""
import sys

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def rename_state_two(username, password, database):
    """Change the name of the State whose id is 2 to New Mexico."""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = session.query(State).filter(State.id == 2).first()
    if state is not None:
        state.name = "New Mexico"
        session.commit()
    session.close()


if __name__ == "__main__":
    rename_state_two(sys.argv[1], sys.argv[2], sys.argv[3])
