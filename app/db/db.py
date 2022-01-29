# Imports
from flask_mongoengine import MongoEngine
from app.run import app

# db config
app.config['MONGODB_SETTINGS'] = {
    'db': 'api_multifile_test',
    'host': 'localhost',
    'port': 27017
}

db = MongoEngine()
db.init_app(app)
