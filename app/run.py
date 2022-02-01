"""
--------------------------
run.py
--------------------------
Author: Joshua Miller
Creation Date: January 29th, 2022

Description: Initialization point for flask app.
app object is created here and all endpoints are imported
"""

# Imports
from flask import Flask

# Create app object
app = Flask(__name__)

# Import endpoints after app object is created
from endpoints.generic import *
from endpoints.generic_device import *
from endpoints.template_test import *

if __name__ == '__main__':
    app.run(debug=True)

