#!/usr/bin/python3
"""Display the states matching a name given as argument using MySQLdb."""
import sys

import MySQLdb


def filter_states(username, password, database, state_name):
    """Print the states whose name equals state_name, sorted by id.

    The query is built with format, so it is open to SQL injection on purpose.
    BINARY makes the comparison case sensitive.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = BINARY '{}' "
                   "ORDER BY id ASC".format(state_name))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
