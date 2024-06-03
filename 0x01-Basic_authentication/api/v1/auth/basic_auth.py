#!/usr/bin/env python3
"""this module for basic authentication"""
from api.v1.auth.auth import Auth
from base64 import b64decode, decode
from typing import Tuple, TypeVar
from models.user import User


class BasicAuth(Auth):
    """initialized basic authentication"""

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """
        Returns:
            the Base64 part of the Authorization header
            for a Basic Authentication
        """
        if not authorization_header or \
                not isinstance(authorization_header, str) or \
                authorization_header[:5] != 'Basic':
            return None
        value = authorization_header.split(" ")
        return value[1] if len(value) > 1 else None

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """Return:
            The decoded value of a Base64 string
                base64_authorization_header
        """
        if not base64_authorization_header or \
                not isinstance(base64_authorization_header, str):
            return None

        try:
            data_bytes = b64decode(base64_authorization_header)
        except Exception:
            return None
        return data_bytes.decode('utf-8')

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> Tuple[str, str]:
        """Return:
            The user email and password
            from the Base64 decoded value.
        """
        if not decoded_base64_authorization_header or\
                not isinstance(decoded_base64_authorization_header, str) or\
                ":" not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(":"))

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """The User instance based on his email and password."""
        if not user_email or \
                not isinstance(user_email, str) or \
                not user_pwd or \
                not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
            if len(users) and users[0].is_valid_password(user_pwd):
                return users[0]
        except Exception:
            pass
        return None
