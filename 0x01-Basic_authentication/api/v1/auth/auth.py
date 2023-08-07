#!/usr/bin/env python3
"""
define Auth class
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    a template for all authentication system
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determine if authentication is required for a given path.
        """
        if path is None:
            return True

        if excluded_paths is None:
            return True

        if path in excluded_paths:
            return False

        path = path.rstrip('/')
        for excluded_path in excluded_paths:
            excluded_path = excluded_path.rstrip('/')
            if path == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieve the authorization header from a Flask request.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieve the current user associated with a Flask request.
        """
        return None
