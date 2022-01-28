# Imports
import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)

# db config
app.config['MONGODB_SETTINGS'] = {


}
db = MongoEngine()
db.init_app(app)

# Endpoints
@app.route('/')
def home():
    return '<p> hello world </p>'

@app.route('/device', methods=['GET'])
def get_device():

@app.route('/device', methods=['PUT'])
def create_device():

@app.route('/device', methods=['POST'])
def update_device():

@app.route('/device', methods=['DELETE'])
def delete_device():


# Classes
class Command(db.Document):
    id = db.StringField()
    target = db.StringField()
    time =
    type =  # is it a power or a configuration command (enumerate command types)
    payload =

class Device(db.Document):
    id =
    ip_address =
    type =
    status =

class DeviceStatus(db.Document):
    device_id =
