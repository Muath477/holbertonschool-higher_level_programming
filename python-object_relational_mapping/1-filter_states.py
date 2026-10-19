#!/usr/bin/python3
"""List the states whose name starts with an upper case N using MySQLdb."""
import sys

import MySQLdb


def list_n_states(username, password, database):
    """Print the states starting with N, sorted by ascending id.

    LIKE BINARY makes the match case sensitive, so only an upper case N counts.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' "
                   "ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_n_states(sys.argv[1], sys.argv[2], sys.argv[3])
