#!/usr/bin/python3
""" deletes all State objects with a name containing
    the letter a from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """ deletes all State objects with a name """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    condition = State.name.like('%a%')
    deleted_count = session.query(State).filter(condition).delete(synchronize_session=False)
    session.commit()

    session.close()


if __name__ == "__main__":
    main()
