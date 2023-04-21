#!/usr/bin/python3
""" a script that adds the State object “Louisiana” to
the database hbtn_0e_6_usa"""

from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print("{} username password database name required".format(args[0]))
        sys.exit(1)

    username = args[1]
    password = args[2]
    database = args[3]

    # create a connection to the db
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    # session factory
    Session = sessionmaker(bind=engine)

    # create a session
    session = Session()

    # new state add
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    # Print the new state object's id
    print(new_state.id)
