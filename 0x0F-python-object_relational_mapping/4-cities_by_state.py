#!/usr/bin/python3
""" Lists all cities from the hbtn_0e_0_usa database.

Usage:
    ./4-cities_by_state <username> <passwd> <database>

"""

from sys import argv
import MySQLdb as mdb


if __name__ == "__main__":
    db = mdb.connect("localhost", argv[1], argv[2], argv[3])
    cur = db.cursor()

    cur.execute(
        "SELECT c.id, c.name, s.name \
        FROM cities AS c JOIN states AS s \
        ON c.state_id = s.id"
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
