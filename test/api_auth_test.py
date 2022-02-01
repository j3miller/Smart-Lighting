"""
--------------------------
api_auth_test.py
--------------------------
Author: Joshua Miller
Creation Date: February 1st, 2022

Description: Script to test the auth key implementation
for the smart api
"""

# Imports
import requests
import json
import os

# Requests variables
localhost_url = 'http://localhost:5000/'
url = localhost_url
headers = {
    'Content-Type': 'application/json'
}
api_key = os.environ.get("SMART_API_KEY")


# Helper function for printing json response
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def get_device_auth_test():
    print("============================")
    print("Starting Get Device Test")
    print("============================")

    # URL for device endpoint
    device_url = url + "device"

    # Build initial payload for test
    device_name = 'get_auth_test_device'
    ip_address = '0.0.0.0'
    payload = '{"api_key": "%s", "device_name": "%s", "ip_address": "%s"}' % (api_key, device_name, ip_address)

    # Put test device in database
    print("Creating test device . . . ")
    response = requests.put(url=device_url, headers=headers, data= payload)
    print("Got response from create device endpoint: ", response)
    jprint(response.json())

    # Test get device endpoint with no auth
    print("Testing get device - NO AUTH")
    payload = {'device_name': device_name}
    response = requests.get(url=device_url, params=payload)
    print("Got response from get device endpoint: ", response)
    jprint(response.json())

    # Test get device endpoint with bad auth
    print("Testing get device - BAD AUTH")
    payload = {'api_key': '1234', 'device_name': device_name}
    response = requests.get(url=device_url, params=payload)
    print("Got response from get device endpoint: ", response)
    jprint(response.json())

    # Test get device endpoint with good auth
    print("Testing get device - GOOD AUTH")
    payload = {'api_key': api_key, 'device_name': device_name}
    response = requests.get(url=device_url, params=payload)
    print("Got response from get device endpoint: ", response)
    jprint(response.json())

    # Clean up
    print("Cleaning up . . .")
    payload = '{"api_key": "%s", "device_name": "%s"}' % (api_key, device_name)
    response = requests.delete(url=device_url, headers=headers, data=payload)
    print("Got response from delete device endpoint: ", response)
    jprint(response.json())


def create_device_auth_test():
    print("============================")
    print("Starting Create Device Test")
    print("============================")

    # URL for device endpoint
    device_url = url + "device"

    # Build initial payload for test
    device_name = 'create_auth_test_device'
    ip_address = '0.0.0.0'

    # Test create device endpoint with no auth
    print("Testing create device - NO AUTH")
    payload = '{"device_name": "%s", "ip_address": "%s"}' % (device_name, ip_address)
    response = requests.put(url=device_url, headers=headers, data= payload)
    print("Got response from create device endpoint: ", response)
    jprint(response.json())

    # Test create device endpoint with bad auth
    print("Testing create device - BAD AUTH")
    payload = '{"api_key": "1234", "device_name": "%s", "ip_address": "%s"}' % (device_name, ip_address)
    response = requests.put(url=device_url, headers=headers, data= payload)
    print("Got response from create device endpoint: ", response)
    jprint(response.json())

    # Test create device endpoint with good auth
    print("Testing create device - GOOD AUTH")
    payload = '{"api_key": "%s", "device_name": "%s", "ip_address": "%s"}' % (api_key, device_name, ip_address)
    response = requests.put(url=device_url, headers=headers, data= payload)
    print("Got response from create device endpoint: ", response)
    jprint(response.json())

    # Clean up
    print("Cleaning up . . .")
    payload = '{"api_key": "%s", "device_name": "%s"}' % (api_key, device_name)
    response = requests.delete(url=device_url, headers=headers, data=payload)
    print("Got response from delete device endpoint: ", response)
    jprint(response.json())


def update_device_auth_test():
    print("============================")
    print("Starting Update Device Test")
    print("============================")

    # URL for device endpoint
    device_url = url + "device"

    # Build initial payload for test
    device_name = 'update_auth_test_device'
    ip_address = '0.0.0.0'
    payload = '{"api_key": "%s", "device_name": "%s", "ip_address": "%s"}' % (api_key, device_name, ip_address)
    # Create device to be updated
    print("Creating device")
    response = requests.put(url=device_url, headers=headers, data= payload)
    print("Got response from create device endpoint: ", response)
    jprint(response.json())

    # Test update device endpoint - NO AUTH
    new_ip = '1.1.1.1'
    print("Testing update device - NO AUTH")
    payload = '{"device_name": "%s", "ip_address": "%s"}' % (device_name, new_ip)
    response = requests.post(url=device_url, headers=headers, data=payload)
    print("Got response from update device endpoint: ", response)
    jprint(response.json())
    # Verify that data was not changed
    payload = {'api_key': api_key, 'device_name': device_name}
    response = requests.get(url=device_url, params=payload)
    print("Got response from get device endpoint: ", response)
    jprint(response.json())

    # Test update device endpoint - BAD AUTH
    print("Testing update device - BAD AUTH")
    payload = '{"api_key": "1234", "device_name": "%s", "ip_address": "%s"}' % (device_name, new_ip)
    response = requests.post(url=device_url, headers=headers, data=payload)
    print("Got response from update device endpoint: ", response)
    jprint(response.json())
    # Verify that data was not changed
    payload = {'api_key': api_key, 'device_name': device_name}
    response = requests.get(url=device_url, params=payload)
    print("Got response from get device endpoint: ", response)
    jprint(response.json())

    # Test update device endpoint - GOOD AUTH
    print("Testing update device - GOOD AUTH")
    payload = '{"api_key": "%s", "device_name": "%s", "ip_address": "%s"}' % (api_key, device_name, new_ip)
    response = requests.post(url=device_url, headers=headers, data=payload)
    print("Got response from update device endpoint: ", response)
    jprint(response.json())
    # Verify that data was not changed
    payload = {'api_key': api_key, 'device_name': device_name}
    response = requests.get(url=device_url, params=payload)
    print("Got response from get device endpoint: ", response)
    jprint(response.json())

    # Clean up
    print("Cleaning up . . .")
    payload = '{"api_key": "%s", "device_name": "%s"}' % (api_key, device_name)
    response = requests.delete(url=device_url, headers=headers, data=payload)
    print("Got response from delete device endpoint: ", response)
    jprint(response.json())


def delete_device_auth_test():
    print("============================")
    print("Starting Delete Device Test")
    print("============================")

    # URL for device endpoint
    device_url = url + "device"

    # Build initial payload for test
    device_name = 'delete_auth_test_device'
    ip_address = '0.0.0.0'
    payload = '{"api_key": "%s", "device_name": "%s", "ip_address": "%s"}' % (api_key, device_name, ip_address)
    # Create device to be deleted
    print("Creating device")
    response = requests.put(url=device_url, headers=headers, data= payload)
    print("Got response from create device endpoint: ", response)
    jprint(response.json())

    # Test delete device endpoint with no auth
    print("Testing delete device - NO AUTH")
    payload = '{"device_name": "%s"}' % device_name
    response = requests.delete(url=device_url, headers=headers, data=payload)
    print("Got response from delete device endpoint: ", response)
    jprint(response.json())
    # Verify that data was not changed
    payload = {'api_key': api_key, 'device_name': device_name}
    response = requests.get(url=device_url, params=payload)
    print("Got response from get device endpoint: ", response)
    jprint(response.json())

    # Test delete device endpoint with bad auth
    print("Testing delete device - BAD AUTH")
    payload = '{"api_key": "1234", "device_name": "%s"}' % device_name
    response = requests.delete(url=device_url, headers=headers, data=payload)
    print("Got response from delete device endpoint: ", response)
    jprint(response.json())
    # Verify that data was not changed
    payload = {'api_key': api_key, 'device_name': device_name}
    response = requests.get(url=device_url, params=payload)
    print("Got response from get device endpoint: ", response)
    jprint(response.json())

    # Test delete device endpoint with GOOD AUTH
    print("Testing delete device - GOOD AUTH")
    payload = '{"api_key": "%s", "device_name": "%s"}' % (api_key, device_name)
    response = requests.delete(url=device_url, headers=headers, data=payload)
    print("Got response from delete device endpoint: ", response)
    jprint(response.json())
    # Verify that data was not changed
    payload = {'api_key': api_key, 'device_name': device_name}
    response = requests.get(url=device_url, params=payload)
    print("Got response from get device endpoint: ", response)
    jprint(response.json())


def main():
    get_device_auth_test()
    print()
    create_device_auth_test()
    print()
    update_device_auth_test()
    print()
    delete_device_auth_test()


if __name__ == '__main__':
    main()
