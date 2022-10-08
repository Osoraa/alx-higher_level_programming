#!/usr/bin/python3
""" Lists all states from the hbtn_0e_6_usa db using SQLAlchemy.

Usage:
    ./7-model_state_fetch_all <user> <passwd> <database>

"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    db_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(db_url)

    result = engine.execute(f"SELECT * from {State.__tablename__}")

    for row in result:
        print(*row, sep=": ")

    # session = engine.connect()
    # session.execute(f"select * from {State}")
