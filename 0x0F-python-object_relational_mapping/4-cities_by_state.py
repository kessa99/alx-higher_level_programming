#!/usr/bin/python3
"""Cities 
by states.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db_nm = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=usr, password=pwd, db=db_nm)

    cursor = db.cursor()
    query = "SELECT cities.id, cities.name,
    states.name FROM cities JOIN states ON cities.state_id = states.id"

    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()
