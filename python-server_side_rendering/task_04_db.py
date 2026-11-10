#!/usr/bin/python3
"""Flask app that shows products from a JSON file, a CSV file or SQLite."""
import csv
import json
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    """Home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """About page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Show every item from items.json, or a message when there are none."""
    try:
        with open('items.json', 'r', encoding='utf-8') as file:
            item_list = json.load(file).get('items', [])
    except (OSError, ValueError):
        item_list = []
    return render_template('items.html', items=item_list)


def read_json():
    """Return the products stored in products.json."""
    with open('products.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def read_csv():
    """Return the products stored in products.csv.

    csv gives every field back as text, so id and price are converted to
    match the JSON data.
    """
    products = []
    with open('products.csv', 'r', encoding='utf-8', newline='') as file:
        for row in csv.DictReader(file):
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


def read_sql():
    """Return the rows of the Products table in products.db as dicts."""
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    try:
        rows = conn.execute(
            'SELECT id, name, category, price FROM Products').fetchall()
    finally:
        conn.close()
    return [dict(row) for row in rows]


@app.route('/products')
def products():
    """Show products from ?source=json, csv or sql, filtered by ?id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    readers = {'json': read_json, 'csv': read_csv, 'sql': read_sql}
    if source not in readers:
        return render_template('product_display.html', error='Wrong source')

    try:
        product_list = readers[source]()
    except sqlite3.Error:
        return render_template('product_display.html',
                               error='Database error')
    except (OSError, ValueError, KeyError):
        message = 'Could not read the {} file'.format(source)
        return render_template('product_display.html', error=message)

    if product_id is not None:
        product_list = [p for p in product_list if str(p['id']) == product_id]
        if not product_list:
            return render_template('product_display.html',
                                   error='Product not found')

    return render_template('product_display.html', products=product_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
