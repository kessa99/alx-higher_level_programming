#!/usr/bin/python3
"""Cities by states"""

import MySQLdb
import sys

if __name__ == 'main':
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db_nm = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=usr, password=pwd, db=db_nm)
    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities, states WHERE states.id=cities.state_id ORDER BY id ASC;"
    cursor.execute(query)

    result = db.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()
