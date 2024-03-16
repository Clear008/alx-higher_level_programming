#!/usr/bin/python3
""" the class definition of a State """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City



class State(Base):
    """Represents a state for a MySQL database."""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship("City", cascade="all, delete", backref="state")
