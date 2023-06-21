#!/usr/bin/python3
"""
    SQL injection
"""

import sys
import MySQLdb

if __name__ == '__main__':
    """
    first open conect database
    """
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], password=sys.argv[2], db=sys.argv[3])

    """
    creat the cursor
    """
    cursor = db.cursor()

    """
    creat option of cursor
    """
    query = "SELECT *FROM states WHERE name = %s"

    """
    Executer l'option
    """
    cursor.execute(query, (sys.argv[4],))

    """
    creer une boucle pour afficher les elements
    """
    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db.close()
