"""
Utility file to store Custom Exception and Function
"""


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
