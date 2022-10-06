#!/usr/bin/python
from sys import argv
import MySQLdb as mdb

cur = mdb.connect("localhost", argv[1], argv[2], argv[3]).cursor()

cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%'")

for row in cur.fetchall():
    print(row)
