from flask import request
from werkzeug.exceptions import Unauthorized

from python_challenge.helpers.decorators.base_decorator import Decorator


def auth(decorated):
    return Auth(decorated)()


class Auth(Decorator):

    def __init__(self, decorated):
        super().__init__(decorated)

    def func_decorator(self, func=None):
        if func is None:
            func = self.decorated

        def wrapper(obj, **kwargs):
            auth_header = request.headers.get('Authorization')
            if auth_header is None:
                raise Unauthorized()
            return func(obj, **kwargs)
        self._copy_custom_attr(func, wrapper)
        return wrapper

    def class_decorator(self):
        # decorate http methods
        decorate_functions = ['get', 'post', 'put', 'delete']

        for f in decorate_functions:
            if hasattr(self.decorated, f):
                setattr(self.decorated, f, self.func_decorator(getattr(self.decorated, f)))

        return self.decorated
