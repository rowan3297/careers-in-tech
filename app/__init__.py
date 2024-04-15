from flask import Flask
from config import DevConfig
#from flask_pymongo import PyMongo

# instantiate flask app
app = Flask(__name__)

# apply configuration
app.config.from_object(DevConfig)

# connect to the database
#mongo = PyMongo(app)

# import routes
from app import routes
