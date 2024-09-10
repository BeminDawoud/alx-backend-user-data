#!/usr/bin/env python3
"""auth module
"""

from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """turns a password into bytes"""
    return hashpw(password.encode("utf-8"), gensalt())
