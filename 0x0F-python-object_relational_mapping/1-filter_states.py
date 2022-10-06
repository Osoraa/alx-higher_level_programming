#!/usr/bin/python
from sys import argv
import MySQLdb as mdb

# Selects all rows from hbtn_0e_0_usa where states.name starts with N
cur = mdb.connect("localhost", argv[1], argv[2], argv[3]).cursor()

cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%'")

for row in cur.fetchall():
    print(row)
