"""
--------------------------
generic_device.py
--------------------------
Author: Joshua Miller
Creation Date: January 29th, 2022

Description: Class definition for basic device object
"""

# Imports
from app.db.db import db


# Classes
class Device(db.Document):
    device_name = db.StringField()
    ip_address = db.StringField()

    def to_json(self):
        return {
            "device_name": self.device_name,
            "ip_address": self.ip_address
        }
