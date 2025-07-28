from flask_pymongo import PyMongo
from bson.json_util import dumps
from flask import current_app
import os

from dotenv import load_dotenv
load_dotenv()

from flask import Flask

# Temporary app instance for MongoDB setup
app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

# Connect to the "incidents" collection
incident_collection = mongo.db.get_collection("incidents")

# Function to log a new incident
def log_incident(data):
    return incident_collection.insert_one(data)

# Function to get all incidents
def get_all_incidents():
    incidents = incident_collection.find()
    return eval(dumps(incidents))  # safely convert BSON to Python dict
