
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from db import initialize_mongo,ensure_collections
from models import log_incident, get_all_incidents

# Load environment variables for local development
load_dotenv()

# Import the mongo instance from our new db.py

app = Flask(_name_)
CORS(app)

mongo_uri = os.getenv("MONGO_URI")

# Add a check to ensure the URI is not None
if not mongo_uri:
    raise ValueError("MONGO_URI environment variable not set!")

app.config["MONGO_URI"] = mongo_uri

# Initialize the mongo object with our app
mongo = initialize_mongo(app)

# Ensure collections are created (must be called inside app context)
with app.app_context():
    ensure_collections(mongo)


# --- Routes ---
@app.route('/')
def home():
    return "✅ Incident Tracker Flask App is Running"

@app.route('/incident', methods=['POST'])
def create_incident():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    result = log_incident(mongo,data)
    return jsonify({"message": "Incident logged", "id": str(result.inserted_id)}), 201

@app.route('/incidents', methods=['GET'])
def get_incidents():
    incidents = get_all_incidents(mongo)
    return jsonify(incidents), 200
