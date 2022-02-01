"""
--------------------------
auth.py
--------------------------
Author: Joshua Miller
Creation Date: January 29th, 2022

Description: handler for API key verification

"""

import os


class _AuthHandler:
    __API_KEY = os.environ.get("SMART_API_KEY")

    def auth_check(self, test_key):
        if test_key == self.__API_KEY:
            return True
        else:
            return False


check = _AuthHandler()
