#!/usr/bin/python3
"""List all the cities of a state given as argument, using MySQLdb."""
import sys

import MySQLdb


def filter_cities(username, password, database, state_name):
    """Print the cities of state_name on one line, separated by commas.

    The state name is passed as a query parameter, so the script is safe from
    SQL injection. A state without cities prints an empty line.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities "
                   "JOIN states ON cities.state_id = states.id "
                   "WHERE states.name = %s ORDER BY cities.id ASC",
                   (state_name,))
    print(", ".join(row[0] for row in cursor.fetchall()))
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_cities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
