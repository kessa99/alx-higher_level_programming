#!/usr/bin/python3
"""SQL injection"""

import MySQLdb
import sys


if __name__ == '__main__':
    """first open conect database"""
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db_nm = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=usr, password=pwd, db=db_nm)

    """creat the cursor"""
    cursor = db.cursor()

    """creat option of cursor"""
    query = "SELECT * FROM states WHERE name = %s"

    """Executer l'option"""
    cursor.execute(query, (sys.argv[4],))

    """creer une boucle pour afficher les elements"""
    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db.close()
