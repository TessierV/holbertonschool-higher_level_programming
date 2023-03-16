#!/usr/bin/python3
""" lists all State objects from the database """

import MySQLdb
import sys


if __name__ == '__main__':

    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    resultfetch = cursor.fetchall()

    for i, row in enumerate(resultfetch):
        if i > 0:
            print(', ', end='')
        print(str(row[1]), end='')
    print()

    cursor.close()
    db.close()
