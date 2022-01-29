from flask import Flask
app = Flask(__name__)
from endpoints.generic import *
from endpoints.generic_device import *

if __name__ == '__main__':
    app.run(debug=True)

