#!/usr/bin/python3
"""Add the State Louisiana to a MySQL database using SQLAlchemy."""
import sys

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def add_louisiana(username, password, database):
    """Insert the State Louisiana and print the id it was given."""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = State(name="Louisiana")
    session.add(state)
    session.commit()
    print(state.id)
    session.close()


if __name__ == "__main__":
    add_louisiana(sys.argv[1], sys.argv[2], sys.argv[3])
