#!/usr/bin/python3
""" Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument. But this time,
write one that is safe from MySQL injections """

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

    cursor.execute("""SELECT * FROM states WHERE name \
                = % s ORDER BY states.id ASC""", (sys.argv[4],))

    resultfetch = cursor.fetchall()
    for row in resultfetch:
        print(row)
    cursor.close()
    db.close()
