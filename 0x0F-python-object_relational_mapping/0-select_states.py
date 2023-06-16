import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(user = username,
        password = password, db = database)
    cursor = db.cursor()
    query = "SELECT *FROM states ORDER BY id ASC"
    cursor.execute(query)

    result = cursor.ferchall()
    for row in result:
        print(row)

    cursor.close()
    db.close()
