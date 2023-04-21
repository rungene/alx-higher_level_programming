#!/usr/bin/python3
"""hat prints all City objects from the database hbtn_0e_14_usa"""

from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_city import City

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

    # Query the db
    states_city = session.query(State, City).join(State)\
                         .order_by(City.id).all()

    # Print results
    for state, city in states_city:
        print(f'{state.name}: {(city.id)} {city.name}')
