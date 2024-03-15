#!/usr/bin/python3
""" the class definition of a city """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State, Base


Base = declarative_base()


class City(Base):
    """Represents a city for a MySQL database."""

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('shbtn_0e_4_usa.satates.id'), nullable=False)
