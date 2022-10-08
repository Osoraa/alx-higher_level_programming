#!/usr/bin/python3
""" Prints the first state object from a database

Usage:
    ./8-model_state_fetch_first <user> <passwd> <database>

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
        result = session.query(State).first()

    if not result:
        print("Nothing")
    else:
        print(result.id, result.name, sep=": ")
