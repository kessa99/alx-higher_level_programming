#!/usr/bin/python3
"""all cities by states"""

import MySQLdb
import sys


if __name__ == '__main':
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db_nm = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=usr, password=pwd, db=db_nm)
    cursor = db.cursor()
    query = "SELECT *FROM cities WHERE name;"
    cursor.execute(query, (sys.argv[4],))

    result = cursor.fetchall()
    for raw in result:
        print(row)

    cursor.close();
    clone.db()
