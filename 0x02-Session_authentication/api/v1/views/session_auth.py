#!/usr/bin/env python3
""" Module of Session authentication
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login():
    """
    Handle user login using Session authentication.
    Response: JSON response with user information and session cookie.
    """
    from api.v1.app import auth
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    matching_users = User.search(attributes={'email': email})
    if not matching_users:
        return jsonify({"error": "no user found for this email"})

    for user in matching_users:
        if user.is_valid_password(password):
            session_id = auth.create_session(user.id)
            response_data = user.to_json()
            response = jsonify(response_data)
            response.set_cookie(
                    os.environ.get('SESSION_NAME'), session_id
                    )

            return response

    return jsonify({"error": "wrong password"}), 401
