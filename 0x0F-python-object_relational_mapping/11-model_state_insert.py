#!/usr/bin/python3
""" Adds the State object “Louisiana” to the database  """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """ Adds the State to the database """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    state = session.query(State).filter(State.name == 'Louisiana').first()
    print("{}".format(state.id))
    session.close()


if __name__ == "__main__":
    main()
