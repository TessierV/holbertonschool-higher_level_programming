#!/usr/bin/python3
"""  name of a state as an argument and lists
all cities of that state """

import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cursor = db.cursor()

    cursor.execute("""SELECT cities.name
                   FROM cities JOIN states
                    ON states.id = cities.state_id WHERE states.name
                   = % s ORDER BY cities.id ASC""", (sys.argv[4],))
    resultfetch = cursor.fetchall()

    for i, row in enumerate(resultfetch):
        if i > 0:
            print(', ', end='')
        print(str(row[0]), end='')
    print()

    cursor.close()
    db.close()
