#!/usr/bin/python3
"""
Get a state
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlachemy import create_engine

if __name__ == '__main__':
    """
    Connexion to server
    """
    engine = create_engine('mysql://{}: {}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))

