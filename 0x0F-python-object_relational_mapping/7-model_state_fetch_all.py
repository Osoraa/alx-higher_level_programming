#!/usr/bin/python3
""" Lists all states from the hbtn_0e_6_usa db using SQLAlchemy.

Usage:
    ./7-model_state_fetch_all.py <user> <passwd> <database>

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
        print(row.id, row.name, sep=": ")
