"""
--------------------------
basic_api_test.py
--------------------------
Author: Joshua Miller
Creation Date: January 29th, 2022

Description: Script to automate testing of
generic device endpoints, and verify functionality of
backend and database implementation
"""

# Imports
import requests
import json

# requests variables
localhost_url = 'http://localhost:5000/'
# local_net_url =
url = localhost_url
headers = {
    'Content-Type': 'application/json',
}


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def device_endpoint_test():
    # URL for device endpoint
    device_url = url + "device"

    # Build initial payload for test
    device_name = "test device"
    ip_address = "0.0.0.0"
    payload = '{"device_name": "%s", "ip_address": "%s"}' % (device_name, ip_address)

    # Test Create Device Endpoint
    print("============================")
    print("Starting Create Device Test")
    print("============================")
    response = requests.put(url=device_url, headers=headers, data=payload)
    print("Got response from create device endpoint: ", response)
    jprint(response.json())

    # Test Get Device Endpoint
    print("============================")
    print("Starting Get Device Test")
    print("============================")
    payload = {"device_name": device_name}
    response = requests.get(url=device_url, params=payload)
    print("Got response from get device endpoint: ", response)
    jprint(response.json())

    # Test Update Device Endpoint
    print("============================")
    print("Starting Update Device Test")
    print("============================")
    new_ip = '1.1.1.1'
    payload = '{"device_name": "%s", "ip_address": "%s"}' % (device_name, new_ip)
    response = requests.post(url=device_url, headers=headers, data=payload)
    print("Got response from update device endpoint: ", response)
    jprint(response.json())

    # Test Delete Device Endpoint
    print("============================")
    print("Starting Delete Device Test")
    print("============================")
    payload = '{"device_name": "%s"}' % device_name
    response = requests.delete(url=device_url, headers=headers, data=payload)
    print("Got response from delete device endpoint: ", response)
    jprint(response.json())


def main():
    device_endpoint_test()


if __name__ == "__main__":
    main()
