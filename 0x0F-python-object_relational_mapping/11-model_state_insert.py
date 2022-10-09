#!/usr/bin/python3
"""Insertion script using SQLAlchemy.

Inserts a single State object into a database.

Example:
    $ ./11-model_state_insert.py <db_user> <db_passwd> <database>

"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    db_url = f"mysql://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    s = State(name="Louisiana")

    with Session() as session:
        session.add(s)
        session.commit()
        print(s.id)
