"""
--------------------------
template_test.py
--------------------------
Author: Joshua Miller
Creation Date: February 1st, 2022

Description: Testing for rendering templates, CSS, Bootstrap, JS
and all that jazz
"""

# Imports
from flask import render_template
from app.run import app


# Endpoints
@app.route('/test_template')
def test_template():
    return render_template('test.html')


@app.route('/test_base_template')
def test_base_template():
    return render_template('test_base.html')
