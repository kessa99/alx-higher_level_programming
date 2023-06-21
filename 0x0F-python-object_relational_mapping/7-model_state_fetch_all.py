#!/usr/bin/python3

"""
list state objects from the database
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == '__main__':
    """
    creaton de l'engine pour la connexion au server
    """
    engine = create_engine('mysql://{}: {}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))

    #creation de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    #Recuperation de tous les objets State
    states = session.query(State).order_by(State.id).all()

    #Affichage des resultats
    for state in states:
        print("{}: {}".format(state.id, state.name))

    #Fermeture de la session
    session.close()
