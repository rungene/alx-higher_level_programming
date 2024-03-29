#!/usr/bin/python3
"""a script that prints the first State object from the database hbtn_0e_6_usa"""

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

    # construct the query
    states = session.query(State).order_by(State.id.asc())

    # retrive the first result
    result = states.first()

    # Print results
    if result:
        print(f'{result.id}: {result.name}')
    else:
        print('Nothing')
