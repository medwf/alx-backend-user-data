#!/usr/bin/env python3
"""this module for basic authentication"""
from api.v1.auth.auth import Auth
from base64 import b64decode, decode


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
