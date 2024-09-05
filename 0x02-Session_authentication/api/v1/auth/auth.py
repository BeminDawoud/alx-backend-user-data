#!/usr/bin/env python3
""" Auth module
"""
from typing import List, TypeVar
from flask import request
import os


class Auth():
    """ Auth Class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        ''' checks if a path requires authentication
        '''
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if not path.endswith('/'):
            path += '/'
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        ''' returns None
        '''
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        ''' returns None
        '''
        return None

    def session_cookie(self, request=None):
        ''' Returns cookie value from a request
        '''
        if request is None:
            return None
        cookie_name = os.getenv('SESSION_NAME')
        return request.cookies.get(cookie_name)
