#!/usr/bin/python3
"""Flask app that lists items read from items.json."""
import json

from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
