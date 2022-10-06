#!/usr/bin/python
""" Lists all states from the hbtn_0e_0_usa database.

Usage:
    ./0-select_states.py <user> <passwd> <database>
"""

from sys import argv
import MySQLdb as mdb


if __name__ == "__main__":
    db = mdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306
    )
    cur = db.cursor()

    cur.execute("SELECT * FROM states")
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
