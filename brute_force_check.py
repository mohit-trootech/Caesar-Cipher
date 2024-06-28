"""
a brute-force attack consists of an attacker submitting many passwords or passphrases with the hope of eventually
guessing correctly.
This helps you to test your password with available brute force dictionary
"""

from brute_force_attack import brute_force_attack


def main():
    """
    Drive Code
    """
    password = input("Enter Password: ")

    brute_force_attack(password)


if __name__ == "__main__":
    main()
