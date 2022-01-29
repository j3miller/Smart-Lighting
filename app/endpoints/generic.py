"""
--------------------------
generic.py
--------------------------
Author: Joshua Miller
Creation Date: January 29th, 2022

Description: Endpoint/route definitions for generic access and
uncategorized routes
"""

# Imports
from app.run import app


# Generic Endpoints
@app.route('/')
def home():
    return '<p> hello world </p>'
