#!/usr/bin/env python3
"""
define hash_password function
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    returns a salted, hashed password, which is a byte string
    """
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_pwd


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates a password against a hashed password."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
