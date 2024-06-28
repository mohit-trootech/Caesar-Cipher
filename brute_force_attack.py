"""a brute-force attack consists of an attacker submitting many passwords or passphrases with the hope of eventually
guessing correctly."""

import csv
from Python_Learning.time_complexity import check_complexity
from encryption import encryption


@check_complexity
def brute_force_attack(password: str) -> None:
    """
    brute force attack without key
    """
    print("Brute Forcing Hash Password")
    with open("password_data.csv", "r") as fp:
        data = csv.reader(fp)
        for i in range(1, 10):
            for item in data:
                password_hash = encryption(*item, i)
                if password_hash == encryption(password, i):
                    print("Password is Less Secure")
                    print("Found Password", item)
                    return
        else:
            print("Secure Password")


if __name__ == "__main__":
    brute_force_attack("123")
    print(brute_force_attack.__doc__)
    pass
