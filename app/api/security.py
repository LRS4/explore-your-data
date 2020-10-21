""" Security Related things """
from functools import wraps
from flask import request
from flask_restx import abort


def require_auth(func):
    """ 
    Secure method decorator which verifies session ID is present. 
    Returns 401 unauthorised if not present in request.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            if request.get_json()['sessionId'] or request.form['sessionId']:
                return func(*args, **kwargs)
            else:
                return abort(401, message="Must provide auth token.")
        except:
            return abort(401, message="Must provide auth token.")
    return wrapper
