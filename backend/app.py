from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables (like MONGO_URI)
load_dotenv()

from models import log_incident, get_all_incidents

app = Flask(__name__)
CORS(app)  # Allow frontend calls from different origin

# Route: Health Check or Home
@app.route('/')
def home():
    return "✅ Incident Tracker Flask App is Running"

# Route: Log a new incident
@app.route('/incident', methods=['POST'])
def create_incident():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    result = log_incident(data)
    return jsonify({"message": "Incident logged", "id": str(result.inserted_id)}), 201

# Route: Get all incidents
@app.route('/incidents', methods=['GET'])
def get_incidents():
    incidents = get_all_incidents()
    return jsonify(incidents), 200

if __name__ == '__main__':
    app.run(debug=True)
