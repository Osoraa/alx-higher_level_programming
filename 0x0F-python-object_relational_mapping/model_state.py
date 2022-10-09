#!/usr/bin/python3
"""State model init script.

Implements the State Class along with its Super class, Base.

Example:
    $ ./6-model_state.py <user> <passwd> <database>

"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Implementation of the State class."""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
