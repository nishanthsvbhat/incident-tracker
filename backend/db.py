from flask import Flask
from flask_pymongo import PyMongo

def initialize_mongo(app:Flask):
    """
    Initialize the PyMongo instance with the Flask app.
    """
    mongo = PyMongo(app)
    return mongo

def ensure_collections(mongo: PyMongo):
    """
    Ensure that the required collections exist in the MongoDB database.
    """
    if not mongo:
        raise ValueError("Mongo instance is not initialized")
    if mongo.db is None:
        raise ValueError("Mongo database is not initialized")
    # Check if the 'incidents' collection exists, if not create it
    existing_collections = mongo.db.list_collection_names()
    if "incidents" not in existing_collections:
        mongo.db.create_collection("incidents")
