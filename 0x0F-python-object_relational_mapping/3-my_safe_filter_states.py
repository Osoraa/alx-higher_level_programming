#!/usr/bin/python3
from sys import argv
import MySQLdb as mdb

if __name__ == "__main__":
    db = mdb.connect("localhost", argv[1], argv[2], argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name = %s", (argv[4],))
    for row in cur.fetchall():
        if row[1] == argv[4]:
            print(row)

    cur.close()
    db.close()
