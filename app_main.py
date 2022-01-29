"""
--------------------------
app_main.py (***OUTDATED***)
--------------------------
Author: Joshua Miller
Creation Date: January 27th, 2022

Description: First pass at flask app with mongodb database.
This file is ***OUTDATED*** and has been replaced with a
more modular implementation in the 'app/' directory
"""

# Imports
import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)

# db config
app.config['MONGODB_SETTINGS'] = {
    'db': 'api_test_database',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)


# Classes
class Device(db.Document):
    device_name = db.StringField()
    ip_address = db.StringField()

    def to_json(self):
        return {
            "device_name": self.device_name,
            "ip_address": self.ip_address
        }


# Generic Endpoints
@app.route('/')
def home():
    return '<p> hello world </p>'


# Device Endpoints
@app.route('/device', methods=['GET'])
def get_device():
    device_name = request.args.get('device_name')
    device = Device.objects(device_name=device_name).first()
    if not device:
        return jsonify({'error': 'device not found'})
    else:
        return jsonify(device.to_json())


@app.route('/device', methods=['PUT'])
def create_device():
    req = json.loads(request.data)
    device = Device(
        device_name=req['device_name'],
        ip_address=req['ip_address']
    )
    device.save()
    return jsonify(device.to_json())


@app.route('/device', methods=['POST'])
def update_device():
    req = json.loads(request.data)
    device = Device.objects(device_name=req['device_name']).first()
    if not device:
        return jsonify({'error': 'device not found'})
    else:
        device.update(ip_address=req['ip_address'])
    # Need to update device object
    device = Device.objects(device_name=req['device_name']).first()
    return jsonify(device.to_json())


@app.route('/device', methods=['DELETE'])
def delete_device():
    req = json.loads(request.data)
    device = Device.objects(device_name=req['device_name']).first()
    if not device:
        return jsonify({'error': 'device not found'})
    else:
        device.delete()
    return jsonify(device.to_json())
