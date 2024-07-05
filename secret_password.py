"""
using secret choice to generate random password
try brute force attack to check for password security
"""

import secrets
import string
from time import sleep
from brute_force_attack import brute_force_attack


def generate_password():
    character_set = string.ascii_letters + string.digits + string.punctuation
    while True:
        pas = "".join(secrets.choice(character_set) for i in range(64))
        if (
            any([c for c in pas if c in string.ascii_lowercase])
            and any([c for c in pas if c in string.ascii_uppercase])
            and any([c for c in pas if c in string.digits])
            and any([c for c in pas if c in string.punctuation])
        ):
            return pas


if __name__ == "__main__":
    generate_password()
    while True:
        password = generate_password()
        brute_force_attack(password)
        sleep(1)
