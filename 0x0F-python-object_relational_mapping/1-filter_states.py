#!/usr/bin/python3
""" Lists all states starting with N from the hbtn_0e_0_usa database.

Usage:
    ./1-filter_states.py <user> <passwd> <database>
"""

from sys import argv
import MySQLdb as mdb


if __name__ == "__main__":
    db = mdb.connect("localhost", argv[1], argv[2], argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
