#!/usr/bin/python3
"""Display the states matching a name given as argument, safely."""
import sys

import MySQLdb


def safe_filter_states(username, password, database, state_name):
    """Print the states whose name equals state_name, sorted by id.

    The name is passed to execute as a parameter, so MySQLdb escapes it and
    the query cannot be changed by the user input.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                   (state_name,))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    safe_filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
