"""
--------------------------
generic_device.py
--------------------------
Author: Joshua Miller
Creation Date: January 29th, 2022

Description: Endpoint/route definitions for generic
device API. routes are as follows:
    - get device (/device (GET method))
    - create device (/device (PUT method))
    - update device (/device (POST method))
    - delete device (/device (DELETE method))

These endpoints are generic and non-functional, intended as a
blueprint for a more comprehensive implementation
"""

# Imports
import json
from flask import request, jsonify
from app.run import app
from app.classes.generic_device import Device
from app.auth.auth import check


# Device Endpoints
@app.route('/device', methods=['GET'])
def get_device():
    # Check API authentication
    api_key = request.args.get('api_key')
    if not check.auth_check(api_key) or api_key is None:
        return jsonify({'error': 'bad api key'})

    # Handle get device request
    device_name = request.args.get('device_name')
    device = Device.objects(device_name=device_name).first()
    if not device:
        return jsonify({'error': 'device not found'})
    else:
        return jsonify(device.to_json())


@app.route('/device', methods=['PUT'])
def create_device():
    req = json.loads(request.data)
    # Check API authentication
    if 'api_key' in req:
        api_key = req['api_key']
    else:
        api_key = None
    if not check.auth_check(api_key) or api_key is None:
        return jsonify({'error': 'bad api key'})

    # Handle Create Device Request
    device = Device(
        device_name=req['device_name'],
        ip_address=req['ip_address']
    )
    device.save()
    return jsonify(device.to_json())


@app.route('/device', methods=['POST'])
def update_device():
    req = json.loads(request.data)
    # Check API authentication
    if 'api_key' in req:
        api_key = req['api_key']
    else:
        api_key = None
    if not check.auth_check(api_key) or api_key is None:
        return jsonify({'error': 'bad api key'})

    # Handle Update Device Request
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
    # Check API authentication
    if 'api_key' in req:
        api_key = req['api_key']
    else:
        api_key = None
    if not check.auth_check(api_key) or api_key is None:
        return jsonify({'error': 'bad api key'})

    # Handle Delete Device request
    device = Device.objects(device_name=req['device_name']).first()
    if not device:
        return jsonify({'error': 'device not found'})
    else:
        device.delete()
    return jsonify(device.to_json())
