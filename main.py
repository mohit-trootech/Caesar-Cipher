"""
Caesar Cipher: one of the Most Common Cryptography algorithm Used for Encryption and Decryption Process
"""

import constant
from encryption import encryption
from decryption import decryption
from utils import generate_key


def main():
    """
    Driver Code
    """
    try:
        plain_text = input(r"Enter Secret Message: ")
        key = int(input("Please Enter Key: "))
        cipher = encryption(plain_text, generate_key(key))
        print("Cipher Text: ", cipher)
        plain_text = decryption(cipher, generate_key(key))
        print("Decrypted Plain Text: ", plain_text)
    except ValueError as ve:
        print(constant.Key_Error, ve)


if __name__ == "__main__":
    main()
