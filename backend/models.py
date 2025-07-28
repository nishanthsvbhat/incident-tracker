import os
from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)
incident_collection = mongo.db.client.get_database().get_collection("incidents")

def log_incident(title, description):
    incident = {
        "title": title,
        "description": description
    }
    incident_collection.insert_one(incident)

def get_all_incidents():
    incidents = incident_collection.find()
    print(incidents)
    return [{"title": inc["title"], "description": inc["description"]} for inc in incidents]
