#!/usr/bin/env python3
"""
Password hashing utility for PyLink IRC Services.
"""

import getpass

from pylinkirc.coremods.login import pwd_context


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Hashes a password for use with PyLink IRC Services.')
    parser.add_argument('password', help='specifies the password to hash', nargs='?', default='')
    args = parser.parse_args()

    assert pwd_context, 'Cannot hash passwords because passlib is missing! Install it via "pip3 install passlib".'

    password = args.password

    # If no password was given, enter one on the command line
    if not password:
        password = getpass.getpass()

    password = password.strip()
    assert password, "Password cannot be empty!"
    print(pwd_context.hash(password))
