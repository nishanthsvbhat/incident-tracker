# backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Import the mongo instance from our new db.py
from db import mongo

# Load environment variables for local development
load_dotenv()

# --- Main App and Database Setup ---
app = Flask(__name__)
CORS(app)

# Configure the MONGO_URI from environment variables
mongo_uri = os.getenv("MONGO_URI")

# Add a check to ensure the URI is not None
if not mongo_uri:
    # This will stop the app if the MONGO_URI is missing
    raise ValueError("MONGO_URI environment variable not set!")

app.config["MONGO_URI"] = mongo_uri

# Initialize the mongo object with our app
mongo.init_app(app)


# --- Import models AFTER the app and db are configured ---
from models import log_incident, get_all_incidents


# --- Routes ---
@app.route('/')
def home():
    return "✅ Incident Tracker Flask App is Running"

@app.route('/incident', methods=['POST'])
def create_incident():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    result = log_incident(data)
    return jsonify({"message": "Incident logged", "id": str(result.inserted_id)}), 201

@app.route('/incidents', methods=['GET'])
def get_incidents():
    incidents = get_all_incidents()
    return jsonify(incidents), 200
