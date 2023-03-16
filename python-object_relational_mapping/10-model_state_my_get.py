#!/usr/bin/python3
"""
State object with the name passed as argument
"""


import sys
from sqlalchemy.ext.declarative import declarative_base
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(State.name.like(sys.argv[4])
                                         ).order_by(State.id)
    for i in result:
        if i is not None:
            print(f'{i.id}')
        else:
            print('No found')


    session.commit()
    session.close()
