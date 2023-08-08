#!/usr/bin/env python3
"""
define BasicAuth class
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    represents a basic authentication mechanism that extends the
    abstract Auth class.
    """
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """
        Extract the credentials from the 'Authorization' header.
        """
        if authorization_header is None:
            return None

        if not type(authorization_header) is str:
            return None

        if not authorization_header.startswith("Basic "):
            return None
        else:
            return authorization_header[6:]
