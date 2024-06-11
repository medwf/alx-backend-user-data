#!/usr/bin/env python3
"""authentication module"""
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """methods that hashed password"""
    return hashpw(password.encode(), gensalt())
