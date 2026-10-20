#!/usr/bin/python3
"""A simple API built with Flask that stores users in memory."""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Users are kept in memory: {username: user dictionary}. Empty on purpose.
users = {}


@app.route("/")
def home():
    """Return the welcome message of the API."""
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """Return the list of all the usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return OK to show that the API is running."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Return the full object of a user, or 404 if it does not exist."""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a user from the JSON body and return it with a 201 status."""
    new_user = request.get_json(silent=True)
    if not isinstance(new_user, dict):
        return jsonify({"error": "Invalid JSON"}), 400
    username = new_user.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run()
