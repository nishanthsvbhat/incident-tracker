# backend/models.py
from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI")  # Get from Render Env Var

client = MongoClient(MONGO_URI)
db = client["incidentDB"]
collection = db["incidents"]

def add_incident(title, description):
    collection.insert_one({"title": title, "description": description})

def get_all_incidents():
    incidents = collection.find()
    return [{"title": inc["title"], "description": inc["description"]} for inc in incidents]
