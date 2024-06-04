#!/usr/bin/env python3
"""Module class to manage the API authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """class for authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require auth"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        path = path if path[-1] == '/' else f'{path}/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """authorization header"""
        if request is None:
            return None
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None
        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """current user"""
        return None
