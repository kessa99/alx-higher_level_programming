#!/usr/bin/python3
"""
    connect to server
"""

import sys
import subprocess
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    subprocess.call(['mysql', '-u', username, '-p' + 'password', database], stdin=open('0-select_states.sql', 'r'))

    db = MySQLdb.connect(host = 'localhost', port = 3306, user = username,
        password = password, db = database)
    cursor = db.cursor()
    query = "SELECT *FROM states ORDER BY states.id"
    cursor.execute(query)

    result = cursor.ferchall()
    for row in result:
        print(row)

    cursor.close()
    db.close()
