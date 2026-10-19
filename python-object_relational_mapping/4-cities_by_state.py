#!/usr/bin/python3
"""List all the cities of a MySQL database with their state, using MySQLdb."""
import sys

import MySQLdb


def list_cities(username, password, database):
    """Print each city as (id, city name, state name), sorted by city id."""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name "
                   "FROM cities JOIN states ON cities.state_id = states.id "
                   "ORDER BY cities.id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
