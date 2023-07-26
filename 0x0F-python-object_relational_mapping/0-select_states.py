#!/usr/bin/python3
"""
    connect to server
"""

import sys
import MySQLdb

if __name__ == '__main__':
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db_nm = sys.argv[3]

    db = (MySQLdb.connect(host='localhost', port=3306,
                          user=usr, password=pwd, db=db_nm))
    cursor = db.cursor()
    query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(query)

    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db.close()
