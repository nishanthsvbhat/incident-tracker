# backend/db.py

from flask_pymongo import PyMongo

# Create a PyMongo instance that we can initialize later in our main app
mongo = PyMongo()

def ensure_collections():
    # Explicitly create 'incidents' collection if it doesn't exist
    existing_collections = mongo.db.list_collection_names()
    if "incidents" not in existing_collections:
        mongo.db.create_collection("incidents")