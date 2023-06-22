#!/usr/bin/python3
"""
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == '__main__':

    """
    connexion to server
    """
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))

    """
    creation of session
    """
    Session = sessionmaker(bind=engine)

    """
    Option to server
    """
    session = Session()

    """
    option
    """
    opt = session.query(State).filter(State.name.ilike('a%')).all()

    """
    Affichage
    """
    for state in opt:
        print("{}: {}".format(state.id, state.name))
