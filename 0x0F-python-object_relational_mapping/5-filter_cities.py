#!/usr/bin/python3
""" Filters cities by an argument.

Usage:
    ./5-filter_cities <user> <passwd> <database>

"""

from sys import argv
import MySQLdb as mdb


if __name__ == "__main__":
    db = mdb.connect("localhost", argv[1], argv[2], argv[3])
    cur = db.cursor()

    cur.execute(
        "SELECT c.name FROM cities AS c \
        JOIN states AS s ON c.state_id = s.id \
        WHERE s.name = %s", (argv[4],)
    )

    result = [row[0] for row in cur.fetchall()]
    print(", ".join(result))

    cur.close()
    db.close()
