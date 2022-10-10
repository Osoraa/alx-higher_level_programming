#!/usr/bin/python3
"""SQLAlchemy insertion script.

Creates a State with a corresponding City.

Usage:
    $ ./100-relationship_states_cities.py <> <> <>

"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City, Base, State


if __name__ == "__main__":
    db_url = f"mysql://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(db_url)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        result = session.query(State)

    for row in result:
        print(f"{row.id}: {row.name}")
        for city in row.cities:
            print(f"\t{city.id}: {city.name}")
