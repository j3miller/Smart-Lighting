from app.db.db import db
from app.run import app

# Classes
# TODO: the classes should be moved to their own file
class Device(db.Document):
    device_name = db.StringField()
    ip_address = db.StringField()

    def to_json(self):
        return {
            "device_name": self.device_name,
            "ip_address": self.ip_address
        }
