#!/usr/bin/python3
"""City Model init script.

Implements the City class.

Usage:
    $ ./6-model_state.py <user> <passwd> <database>

"""

from sys import argv
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """Implements the City model class"""

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
