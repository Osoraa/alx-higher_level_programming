#!/usr/bin/python3
"""Database query script with SQLAlchemy.

Queries a database for rows matching an argument.

Usage:
    $ ./10-model_state_my_get.py <user> <passwd> <database> <state_name>

"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    db_url = f"mysql://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        try:
            result = session.query(State).filter(State.name == argv[4]).one()
            print(result.id)
        except Exception:
            print("Not found")
