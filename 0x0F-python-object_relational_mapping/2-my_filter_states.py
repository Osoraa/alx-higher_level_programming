#!/usr/bin/python3
"""Lists all states matching a given string.

Usage:
    ./2-my_filter_states <user> <passwd> <database> <query_string>

"""

from sys import argv
import MySQLdb as mdb


if __name__ == "__main__":
    db = mdb.connect("localhost", argv[1], argv[2], argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name = '{:s}'".format(argv[4]))
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
