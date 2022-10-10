#!/usr/bin/python3
"""SQLAlchemy query script.

Prints all City objects from a database.

Usage:
    ./14-model_city_fetch_by_state.py <db_user> <db_passwd> <db_name>

"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import State, City

if __name__ == "__main__":
    db_url = f"mysql://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        result = (session.query(State.name, City.id, City.name).join(City))

    for state_name, city_id, city_name in result:
        print(f"{state_name}: ({city_id}) {city_name}")
