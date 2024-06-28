"""
decryption process for caesarcipher
"""

import constant
from utils import EmptyString


def decryption(msg: str, key: (str, int)) -> str:
    """
    function convert cipher text => plain text
    """
    try:
        key = int(key)
        if not len(msg):
            raise EmptyString(constant.ALNUM_ERROR)
        cipher_text = ""
        for i in msg:
            cipher_text += chr(ord(i) - key)
        return cipher_text.strip()
    except ValueError:
        print(constant.INT_ERROR)
        return
    except EmptyString as es:
        print(es)
        return


if __name__ == "__main__":
    pass
