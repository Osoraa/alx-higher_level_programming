#!/usr/bin/python3
"""Deletion script with SQLAlchemy.

Deletes all entries matching a query from a database.

Usage:
    $ ./13-model_state_delete_a.py <db_user> <db_passwd> <db_name>

"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    db_url = f"mysql://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    with Session.begin() as session:
        session.query(State).filter(State.name.like("%a%")).delete(
            synchronize_session="fetch"
        )
