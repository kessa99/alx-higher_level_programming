#!/usr/bin/python3
"""all cities by states"""

import MySQLdb
import sys


if __name__ == '__main__':
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db_nm = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=usr, password=pwd, db=db_nm)
    cursor = db.cursor()
    query = ("SELECT cities.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s")
    cursor.execute(query, (sys.argv[4],))

    result = cursor.fetchall()
    for raw in result:
        print(raw[0])

    cursor.close()
    db.close()
