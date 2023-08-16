#!/usr/bin/env python3
"""
Start Flask app
"""

from flask import Flask, jsonify, request, abort
from auth import Auth


Auth = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    return welcome message
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """
    Create a new user via a POST request.
    """
    email = request.form['email']
    password = request.form['password']

    try:
        user = Auth.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """
    Perform user login via a POST request.
    """
    form_data = request.form

    if "email" not in form_data:
        return jsonify({"message": "email required"}), 400
    if "password" not in form_data:
        return jsonify({"message": "password required"}), 400

    email = request.form['email']
    password = request.form['password']

    if not Auth.valid_login(email, password):
        abort(401)
    session_id = Auth.create_session(email)
    data = {"email": email, "message": "logged in"}
    response = jsonify(data)
    response.set_cookie('session_id', session_id)

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
