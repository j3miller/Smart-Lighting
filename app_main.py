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
# TODO: the classes should be moved to their own file
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
    device_name = request.args.get('name')
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
    device = Device.objects(name=req['name']).first()
    if not device:
        return jsonify({'error': 'device not found'})
    else:
        device.update(ip_address=req['ip_address'])
    return jsonify(device.to_json())


@app.route('/device', methods=['DELETE'])
def delete_device():
    req = json.loads(request.data)
    device = Device.objects(device_name=req['device_name']).first
    if not device:
        return jsonify({'error': 'device not found'})
    else:
        device.delete()
    return jsonify(device.to_json())

#@app.route('/device/<name>')    # TODO Double check this syntax
#def get_device_status():

# Command Endpoints
#@app.route('/cmd')  # Should only use post for this one
#def send_command():

# Data Endpoints


# Classes
#class Command(db.Document):
#    id = db.StringField()
#    target = db.StringField()
#    time =
#    type =  # is it a power or a configuration command (enumerate command types)
#   payload =

#class Device(db.Document):
#    id =
#    ip_address =
#    type =
#    status =

#class DeviceStatus(db.Document):
#    device_id =
