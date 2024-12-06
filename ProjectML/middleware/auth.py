from functools import wraps
from flask import request

def authMiddleware():
    def _authMiddleware(f):
        @wraps(f)
        def _authMiddleware(*args, **kwargs):
            # just do here everything what you need
            jwt = request.headers.get('Authorization')
            print('before auth middleware', jwt)
            result = f(*args, **kwargs)
            print('middleware result: %s' % result)
            print('after middleware')
            return result
        return _authMiddleware
    return _authMiddleware
