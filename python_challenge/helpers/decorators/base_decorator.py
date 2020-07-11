import inspect
from abc import ABC


class Decorator(ABC):
    """Base decorator class, can be used to create decorators for both classes and functions
    """

    def __init__(self, decorated):
        self.decorated = decorated

    def __call__(self):
        if inspect.isclass(self.decorated):
            return self.class_decorator()
        if inspect.isfunction(self.decorated):
            return self.func_decorator()
        raise Exception

    @staticmethod
    def _copy_custom_attr(origin, dest):
        for attr in dir(origin):
            if attr not in dir(dest):
                __value = getattr(origin, attr)
                setattr(dest, attr, __value)

    def class_decorator(self):
        raise Exception("This decorator is not prepared for classes")

    def func_decorator(self, func=None):
        raise Exception("This decorator is not prepared for functions")
