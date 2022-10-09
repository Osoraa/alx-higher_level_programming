#!/usr/bin/python3
"""Database query script.

Queries a database for rows matching an argument.

Example:
    $ ./9-model_state_filter_a.py <user> <passwd> <database>

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
        result = session.query(State).filter(State.name.like("%a%"))

    for row in result:
        if "a" not in row.name:
            continue
        print(row.id, row.name, sep=": ")
