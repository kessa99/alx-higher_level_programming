#!/usr/bin/python3
"""
    Your script should take 3 arguments: mysql username, mysql p    assword and database name
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running on localhost at port 3306
    Results must be sorted in ascending order by cities.id
    You can use only execute() once
    Results must be displayed as they are in the example below
    Your code should not be executed when imported
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
