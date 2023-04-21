#!/usr/bin/python3
"""a script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa"""

from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 5:
        print("{} username password database name state name\
              to search required".format(args[0]))
        sys.exit(1)

    username = args[1]
    password = args[2]
    database = args[3]
    state_name = args[4]

    # create a connection to the db
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    # session factory
    Session = sessionmaker(bind=engine)

    # create a session
    session = Session()

    # Query State objects from the database sort the results by id
    states = session.query(State).filter(State.name == state_name).first()

    # Print results
    if states:
        print(f'{states.id}')
    else:
        print('Not found')
