# Imports
import json
from flask import request, jsonify
from app.run import app
from app.db.db import db
from app.classes.generic_device import Device


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
