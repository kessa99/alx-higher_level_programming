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
             "WHERE states.name = %s ORDER BY cities.id ASC")
    cursor.execute(query, (sys.argv[4],))

    result = cursor.fetchall()
    for i in range(len(result)):
        print(result[i], end='')
        if i < len(result) - 1:
            print(', ', end='')
    cursor.close()
    db.close()
