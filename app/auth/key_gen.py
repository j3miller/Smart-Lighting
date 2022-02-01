"""
--------------------------
key_gen.py
--------------------------
Author: Joshua Miller
Creation Date: January 29th, 2022

Description: simple script for generating api keys

"""
# Imports
import secrets


def main():
    print(secrets.token_urlsafe(16))


if __name__ == '__main__':
    main()
