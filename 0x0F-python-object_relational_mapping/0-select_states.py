#!/usr/bin/python
from sys import argv
import MySQLdb as mdb

# Connects to and queries the hbtn_0e_0_usa database
db = mdb.connect("localhost", argv[1], argv[2], argv[3])
cur = db.cursor()

cur.execute("SELECT * from states")
for row in cur.fetchall():
    print(row)
