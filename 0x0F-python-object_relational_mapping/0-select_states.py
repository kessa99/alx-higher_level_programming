#!/usr/bin/python3
"""
    connect to server
"""

import sys
import subprocess
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port = 3306, user = sys.argv[1],
        password = sys.argv[2], db = sys.argv[3]
        )
    cursor = db.cursor()
    query = "SELECT *FROM states ORDER BY states.id ASC"
    cursor.execute(query)

    result = cursor.ferchall()
    for row in result:
        print(row)

    cursor.close()
    db.close()
