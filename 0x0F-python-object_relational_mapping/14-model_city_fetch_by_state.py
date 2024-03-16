#!/usr/bin/python3
""" prints all City objects from the database hbtn_0e_14_usa """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main():
    """Print all Cities"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(State.name, City.id, City.name) \
                   .select_from(State) \
                   .join(City, State.id == City.state_id) \
                   .order_by(City.id).all()

    for state_name, city_id, city_name in cities:
        print("{}: ({}) {}".format(state_name, city_id, city_name))

    session.close()


if __name__ == "__main__":
    main()
