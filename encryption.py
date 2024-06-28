"""
encryption process for caesarcipher
"""

import constant
from utils import EmptyString


def encryption(msg: str, key: (str, int)) -> str:
    """
    function convert plain text => cipher text
    """
    try:
        key = int(key)
        if not len(msg):
            raise EmptyString(constant.ALNUM_ERROR)
        cipher_text = ""
        for i in msg:
            cipher_text += chr(ord(i) + key)
        return cipher_text.strip()
    except ValueError:
        print(constant.INT_ERROR)
        return
    except EmptyString as es:
        print(es)
        return


if __name__ == "__main__":
    pass
