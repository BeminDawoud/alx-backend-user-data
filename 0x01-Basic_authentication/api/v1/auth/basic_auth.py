#!/usr/bin/env python3
"""Basic authentication module for the API.
"""
from .auth import Auth


class BasicAuth(Auth):
    """Basic authentication class.
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        '''Returns the Base64 of the Authorization header
        '''
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        if authorization_header.startswith('Basic '):
            return authorization_header[6:]
        else:
            return None