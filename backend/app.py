from flask import Flask, request, jsonify
from flask_cors import CORS
from models import add_incident, get_all_incidents

app = Flask(__name__)
CORS(app)

@app.route("/api/incidents", methods=["GET"])
def list_incidents():
    return jsonify(get_all_incidents())

@app.route("/api/incidents", methods=["POST"])
def create_incident():
    data = request.get_json()
    add_incident(data["title"], data["description"])
    return jsonify({"status": "logged"})
