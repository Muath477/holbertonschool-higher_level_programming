#!/usr/bin/python3
"""A Flask API protected with basic authentication, JWT and roles."""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (JWTManager, create_access_token, get_jwt,
                                jwt_required)
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "change-this-secret-key-before-production"
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1",
              "password": generate_password_hash("password"),
              "role": "user"},
    "admin1": {"username": "admin1",
               "password": generate_password_hash("password"),
               "role": "admin"},
}


@auth.verify_password
def verify_password(username, password):
    """Return the username if the basic auth credentials are valid."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@auth.error_handler
def basic_auth_error():
    """Answer 401 when basic authentication fails."""
    return jsonify({"error": "Unauthorized"}), 401


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Answer 401 when the request has no valid JWT."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Answer 401 when the JWT cannot be decoded."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Answer 401 when the JWT has expired."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Answer 401 when the JWT has been revoked."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Answer 401 when a fresh JWT is required."""
    return jsonify({"error": "Fresh token required"}), 401


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Return a message only to users with valid basic credentials."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Return a JWT for valid credentials, with the role in its claims."""
    data = request.get_json(silent=True) or {}
    user = users.get(data.get("username"))
    if not user or not check_password_hash(user["password"],
                                           data.get("password") or ""):
        return jsonify({"error": "Invalid credentials"}), 401
    token = create_access_token(identity=user["username"],
                                additional_claims={"role": user["role"]})
    return jsonify({"access_token": token})


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Return a message only to requests with a valid JWT."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Return a message only to users whose JWT has the admin role."""
    if get_jwt().get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
