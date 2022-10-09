#!/usr/bin/python3
"""Updation script using SQLAlchemy.

Updates a State entry with state_id = 2 in a database.

Example:
    $ ./12-model_state_update_id_2.py <db_user> <db_passwd> <database>

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
        s = session.query(State).get(2)
        if s is not None:
            s.name = "New Mexico"
            session.add(s)
