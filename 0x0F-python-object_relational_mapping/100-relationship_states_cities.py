#!/usr/bin/python3
""" creates the State “California” with the
City “San Francisco” from the database """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City


def main():
    """Create cities"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
 
    n_state = State(name="California")
    session.add(n_state)
    session.commit()
    n_city = City(name="San Francisco", state_id=n_state.id)
    session.add(n_city)
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
