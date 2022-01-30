# Imports
import os
from app.auth.auth import check

correct_key = os.environ.get("SMART_API_KEY")


def main():
    print(correct_key)
    print("Testing incorrect key")
    print(check.auth_check('bad'))
    print(check.auth_check(correct_key))


if __name__ == '__main__':
    main()
