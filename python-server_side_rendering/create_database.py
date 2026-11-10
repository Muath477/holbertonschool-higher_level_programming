#!/usr/bin/python3
"""Create products.db with the Products table and two sample rows."""
import sqlite3


def create_database():
    """Create the table and insert the sample products.

    INSERT OR REPLACE lets the script run again without failing on the
    primary keys that already exist.
    """
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT OR REPLACE INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_database()
