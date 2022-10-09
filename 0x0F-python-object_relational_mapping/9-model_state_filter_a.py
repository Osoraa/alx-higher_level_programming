#!/usr/bin/python3
""" Queries a database for rows matching an argument

Usage:
    ./9-model_state.py <user> <passwd> <database>

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
        result = session.query(State)

    for row in result:
        if "a" not in row.name:
            continue
        print(row.id, row.name, sep=": ")
