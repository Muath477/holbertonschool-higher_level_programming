#!/usr/bin/python3
"""List all the states of a MySQL database using the MySQLdb module."""
import sys

import MySQLdb


def list_states(username, password, database):
    """Print every row of the states table sorted by ascending id."""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
