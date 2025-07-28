from pymongo import MongoClient
import os

MONGO_URI = os.environ.get("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["incidentDB"]
collection = db["incidents"]

def log_incident(title, description):
    return collection.insert_one({
        "title": title,
        "description": description
    })

def get_all_incidents():
    return list(collection.find({}, {"_id": 0}))
