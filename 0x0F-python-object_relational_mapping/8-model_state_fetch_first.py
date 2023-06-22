#!/usr/bin/python3
"""
filter
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == '__main__':
    """
    Connexion au server avec les arguments
    """
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))

    """
    Liaison a la base de donnee
    """
    Session = sessionmaker(bind=engine)

    """
    Creation d'un instance pour effecter des operation
    """

    session = Session()

    """
    Operation pour afficher le premier
    """

    first_state = session.query(State).first()

    """
    affichage
    """

    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        sys.exit(1)
