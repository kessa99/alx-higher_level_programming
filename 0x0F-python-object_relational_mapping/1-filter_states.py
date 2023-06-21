#!/usr/bin/python3

"""
    Filter element
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port = 3306, user=sys.argv[1], password=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    query = "SELECT *FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    cursor.execute(query)

    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db.close
