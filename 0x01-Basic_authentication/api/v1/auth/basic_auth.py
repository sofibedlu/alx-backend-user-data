#!/usr/bin/env python3
"""
define BasicAuth class
"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """
        Decode base64-encoded credentials from the 'Authorization' header.
        """
        if base64_authorization_header is None:
            return None

        if not type(base64_authorization_header) is str:
            return None

        try:
            credentials = base64_authorization_header
            decoded_credentials = base64.b64decode(credentials).decode('utf-8')
            return decoded_credentials
        except Exception:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """
        Extract user credentials from a decoded Base64-encoded
        'Authorization' header.
        """
        if not decoded_base64_authorization_header:
            return (None, None)

        if not type(decoded_base64_authorization_header) is str:
            return (None, None)

        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        else:
            separated = decoded_base64_authorization_header.split(':')
            return tuple(separated)
