#!/usr/bin/env python3
"""session database authentication"""
from .session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """class SessionDBAuth"""

    def create_session(self, user_id=None):
        """create new session and save session id"""
        session_id = super().create_session(user_id)
        data = dict(self.user_id_by_session_id[session_id])
        data['session_id'] = session_id
        data['created_at'] = data.get(
            'created_at').strftime("%Y-%m-%dT%H:%M:%S")
        user_session = UserSession(**data)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """get user_id from session id"""
        UserSession.load_from_file()
        user_id = super().user_id_for_session_id(session_id)
        return user_id

    def destroy_session(self, request=None):
        """destroy session"""
        session_id = self.session_cookie(request)
        delete_session = UserSession.search({'session_id': session_id})
        if len(delete_session) != 0:
            delete_session[0].remove()
