# backend/models.py

from bson.json_util import dumps
import json

# Import the shared mongo instance from db.py
from db import mongo

# Function to log a new incident
def log_incident(data):
    # Access the collection directly from the shared mongo object
    return mongo.db.incidents.insert_one(data)

# Function to get all incidents
def get_all_incidents():
    incidents_cursor = mongo.db.incidents.find()
    
    # The dumps function from bson.json_util correctly handles
    # MongoDB's BSON types, like ObjectId. We then load it back
    # into a Python object that Flask's jsonify can handle.
    return json.loads(dumps(incidents_cursor))
