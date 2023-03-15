#!/usr/bin/python3
"""task 1"""

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
    for row in resultfetch:
        print(row)
    cursor.close()
    db.close()