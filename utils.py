"""
Utility file to store Custom Exception and Function
"""

from functools import wraps
from time import time


class EmptyString(BaseException):
    def __init__(self, msg):
        super(EmptyString, self).__init__(msg)


def generate_key(key: int) -> int:
    """
    function to generate key: 2**key
    """
    try:
        return 2 ** int(key)
    except ValueError as ve:
        print(constant.KeyError, ve)


def check_complexity(fun):
    """
    Check Time Complexity
    """

    @wraps(fun)
    def inner(*args, **kwargs):
        """
        Wrapper Time Complexity
        """
        before = time()
        result = fun(*args, **kwargs)
        after = time()
        print(
            "Time Taken in {} Complexity: {:.9f}".format(fun.__name__, after - before)
        )
        if result:
            return result

    return inner
