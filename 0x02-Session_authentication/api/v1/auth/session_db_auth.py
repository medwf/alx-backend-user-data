#!/usr/bin/env python3
"""session database authentication"""
from .session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """class SessionDBAuth"""

    def create_session(self, user_id=None):
        """create new session and save session id"""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        data = dict(self.user_id_by_session_id[session_id])
        data['session_id'] = session_id
        data['created_at'] = data.get(
            'created_at').strftime("%Y-%m-%dT%H:%M:%S")
        user_session = UserSession(**data)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """get user_id from session id"""
        try:
            session = UserSession.search({'session_id': session_id})
        except Exception:
            return None
        if len(session) == 0:
            return None
        session = session[0]
        self.user_id_by_session_id[session_id] = {
            'user_id': session.id,
            'created_at': session.created_at
        }
        return super().user_id_for_session_id(session_id)

    def destroy_session(self, request=None):
        """destroy session"""
        session_id = self.session_cookie(request)
        try:
            delete_session = UserSession.search({'session_id': session_id})
        except Exception:
            return False
        if len(delete_session) > 0:
            delete_session[0].remove()
        return False
