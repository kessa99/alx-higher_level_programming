#!/usr/bin/python3

"""
     all cities by states
"""

import sys
import MySQLdb

if __name__ == '__main':

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], password=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    query = "SELECT *FROM cities WHERE name;"
    cursor.execute(query, (sys.argv[4],))

    result = cursor.fetchall()
    for raw in result:
        print(row)

    cursor.close();
    clone.db()
