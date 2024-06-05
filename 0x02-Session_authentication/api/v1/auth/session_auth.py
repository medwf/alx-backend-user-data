#!/usr/bin/env python3
"""this module have a session auth class"""
from .auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """class SessionAuth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create session by user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
