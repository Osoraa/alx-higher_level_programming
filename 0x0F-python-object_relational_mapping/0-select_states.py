#!/usr/bin/python
from sys import argv
import MySQLdb as mdb

db = mdb.connect("localhost", argv[1], argv[2], argv[3])
cur = db.cursor()

cur.execute("SELECT * from states")
for row in cur.fetchall():
    print(row)

# print(argv[1])
