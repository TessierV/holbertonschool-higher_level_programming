#!/usr/bin/python3
"""  lists all cities from the database hbtn_0e_4_usa
"""

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

    cursor.execute("SELECT cities.id, states.name, cities.name \
                   FROM states, cities WHERE states.id = \
                   cities.state_id ORDER BY cities.id ASC")
    resultfetch = cursor.fetchall()

    for row in resultfetch:
        print(row)

    cursor.close()
    db.close()
