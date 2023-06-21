#!/usr/bin/python3
"""
     cities implemetation
"""
import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(host='localhost' ,port=3306, user=sys.argv[1], password=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    query = "SELECT *FROM cities ORDER BY cities.id ASC;"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row);

    cursor.close()
    db.close()
